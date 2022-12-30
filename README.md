# Automated Pokemon Card Tracking/Investing

Poke Track is a Python script that utilizes the Pokemon TCG SDK to help track whether you've made or lost money on your Pokemon Card investments. It does this by looking at the online value of each card if you were to sell versus the total cost of the card.

*** note that this script does not account for selling cards on online stores such as TCG Player that account for 10% sale commission, then 2.5% credit card fee ***

## Getting Started

1. Install [Docker](www.docker.com)
2. Get original [spreadsheet access](https://docs.google.com/spreadsheets/d/1rnqsBE5UIo6HFaGAQSrVzzk18lFTGLS17IVE4oIB4qw/edit?usp=sharing). Then download the new spreadsheet locally
3. Change input and output file paths and file path names then copy run `cp .env.example .env`
4. Run ``` docker-compose up ```
5. Import `poke-spread-w-card_prices.csv` on your spreadsheet as a `new sheet`
6. Copy all data from new sheet onto your main sheet. Right click, paste special, paste only values.

<img src="https://github.com/vverbani/poke-track/blob/main/src/spreadsheet/spreadsheet-screenshot.png" alt="Spreadsheet of Pokemon Card purchases versus online value" title="Spreadsheet of Pokemon Card purchases versus online value">

*** Cards and prices shown in spreadsheet are randomized ***
