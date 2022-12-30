# Automate Picking Pokemon Card Investing

Poke Track is a Python script that utilizes the Pokemon TCG SDK to help track whether you've made or lost money on your Pokemon Card investments. It does this by looking at the online value of each card if you were to sell versus the total cost of the card.

*** note that this script does not account for selling cards on online stores such as TCG Player that account for 10% sale commission, then 2.5% credit card fee ***

## Getting Started

1. Locally install (Docker)[www.docker.com]
2. Create API token from (Pokemon TCG)[https://dev.pokemontcg.io/dashboard] or use Python SDK
3. Get original spreadsheet access. Then download the new spreadsheet locally
4. Change input and output file paths and file path names then copy run `cp .env.example .env`
5. Run ``` docker-compose up ```
6. Import `poke-spread-w-card_prices.csv` on your spreadsheet as a `new sheet`
7. Copy all data from new sheet on your main sheet. Right click, paste special, paste only values.

*** Cards and prices shown in spreadsheet are randomized ***