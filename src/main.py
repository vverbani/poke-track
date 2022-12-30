import os, csv
from dotenv import load_dotenv
from currency_converter import CurrencyConverter

# Pokemon TCG SDK imports
from pokemontcgsdk import Card
from pokemontcgsdk import Set

# Import set names and ID
from helpers.helpers import *

# Load .env file
load_dotenv()

def csv_to_list():
    # Start recording data only after the 4th row ( 0-4 rows should be for the title/headers etc etc)
    temp_csv_list=[]

    # Open the csv file object
    with open(os.getenv('CSV_FILE_WITH_PATH'), 'r') as csv_file:
        # Construct the csv reader object from the file object
        reader= csv.reader(csv_file)

        for row in reader:
            temp_csv_list.append(row)

    # Return a list of csv row objects from the spreadsheet export
    return temp_csv_list

def add_list_to_csv(list):

    # Create `output.csv` and dump our list of organizations in there
    with open(os.getenv('OUTPUT_FINAL_CSV'), 'w') as file:
        # creating a csv writer object
        writer = csv.writer(file, delimiter=',')

        # Insert actual organization data
        for row in list:
            writer.writerow(row)

def card_price_per_set(set):
    # List Example: [{set, average_price, over_10, over_20, over_50, over_100}]
    card_query= ''
    average_price= 0

    # If set contains multiple words, i.e Silver Tempest, Silver Tempest Trainer Gallery add quotes around it other wise call fails
    if len(set.split()) > 1:
        card_query='set.name:' + '"' + set + '"' + ' supertype:pokemon'
    else:
        card_query='set.name:' + set + ' supertype:pokemon'

    cards= Card.where(q=card_query)

    for card in cards:
        # API has some cards at 'None' - potentially because of no sale/list data?
        if card.cardmarket.prices and card.cardmarket.prices.trendPrice:
            average_price += card.cardmarket.prices.trendPrice

    # Needs to change to right currency and round to the nearest cents
    average_price= average_price / len(cards)

    return average_price

def main():
    print("Starting ... .. . . . . . ...")

    temp_set_id= ''
    poke_list= []
    set_price_list= []

    # Prepare currency converter
    currency= CurrencyConverter()

    poke_purchases= csv_to_list()

    for poke in poke_purchases:
        # Only get prices if a Card has a given Description, Set, and a Card number
        if poke[0] != '' and poke[1] == 'Card' and poke[2] != 'n/a' and poke[4] != '':
            # Check to see if set is from Trainer Gallery - amend on its Set code name, i.e swsh12tg-TG20
            for set in set_names:
                if set['name'] == poke[4]:
                    if 'TG' in str(poke[2]):
                        # Example: swsh12tg-TG20
                        temp_set_id= set['id'] + 'tg-' + poke[2]
                    else:
                        # Example: swsh-1
                        temp_set_id= set['id'] + '-' + poke[2]

            card= Card.find(temp_set_id)

            # Convert the price of the card from EUROS (default) into USD then add to row under Online Value (TCG)
            card_price= currency.convert(float(card.cardmarket.prices.trendPrice), 'EUR', 'USD')
            poke[11]= round(card_price,2)

            # Get Unrealized Gains, ie IF you were to sell card
            temp_price= poke[11] - float(poke[10].replace('$',''))

            # Round up to 2 decimal places
            poke[12]= round(temp_price,2)

        # Add each new row to the new list before writing it to the CSV file
        poke_list.append(poke)

    add_list_to_csv(poke_list)

    print("Ending ... .. . . . . . ...")

if __name__ == "__main__":
    main()
