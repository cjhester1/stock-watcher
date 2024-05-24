#api - https://www.alphavantage.co/documentation/#daily

import requests
import creds
#Stock to extract data from

STOCK_NAME = 'TSLA'
COMPANY_NAME = "TESLA INC"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": creds.STOCK_API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
print(response.json())
