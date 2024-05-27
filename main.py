#api - https://www.alphavantage.co/documentation/#daily

import requests
import creds

#Stock name to extract data from
STOCK_NAME = 'TSLA'
COMPANY_NAME = "TESLA INC"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

#API params for time series daily
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": creds.STOCK_API_KEY
}
#testing API response
response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = (response.json()["Time Series (Daily)"])
"""
date is the key  in 'Time series (daily)', we need a way to be able to iterate to the next
key when we fetch tomorrow's data. We can do this using list comprehension
"""
data_list = [value for (key,value) in data.items()]

#print(data_list)

#Yesterdays data will always be in the 0 index
yesterdays_data = data_list[0]

#Yesterday's closing price
yesterdays_closing_price = yesterdays_data["4. close"]

#print(yesterdays_closing_price)


#Day before yesterday's closing price
day_before_yesterdays_data = data_list[1]
#Day before yesterday's closing price
day_before_yesterdays_closing_price = day_before_yesterdays_data["4. close"]

#print(day_before_yesterdays_closing_price)


#Find the positive difference between yesterday and day before yesterday
close_difference = abs(float(day_before_yesterdays_closing_price)-float(yesterdays_closing_price))
#print(close_difference)

#percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percent = (close_difference/float(yesterdays_closing_price)) *100

#print(diff_percent)

#if percentage is greater than 5 then print("Get News").

if diff_percent > 3:
    print("Get News")