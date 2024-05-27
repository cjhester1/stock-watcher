#api - https://www.alphavantage.co/documentation/#daily
import requests
import creds
from twilio.rest import Client

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

#API params for time series daily
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": creds.STOCK_NAME,
    "apikey": creds.STOCK_API_KEY
}
#testing API response
response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()
print(data)
"""
date is the key  in 'Time series (daily)', we need a way to be able to iterate to the next
key when we fetch tomorrow's data. We can do this using list comprehension
"""
data_list = [value for (key,value) in data.items()]

#Yesterdays data will always be in the 0 index
yesterdays_data = data_list[0]
#Yesterday's closing price
yesterdays_closing_price = yesterdays_data["4. close"]

#Day before yesterday's closing price
day_before_yesterdays_data = data_list[1]
#Day before yesterday's closing price
day_before_yesterdays_closing_price = day_before_yesterdays_data["4. close"]


#Find the positive difference between yesterday and day before yesterday
close_difference = (float(day_before_yesterdays_closing_price)-float(yesterdays_closing_price))
#print(close_difference)
up_down = ""
if close_difference > 0:
    up_down = '🔺'
elif close_difference < 0:
    up_down = '🔻'

#percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percent = round(close_difference/float(yesterdays_closing_price)) *100



#if percentage is greater than 5 then print("Get News").
if abs(diff_percent) > 3:
     #print("get news")

    news_params = {
        "apiKey": creds.NEWS_KEY,
        "qInTitle": creds.COMPANY_NAME
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)

    articles = news_response.json()["articles"]

    first_three = articles[:3]

    formatted_article = [f"{creds.STOCK_NAME}:{up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief Description: {article['description']}" for article in first_three]

    client = Client(creds.TWILIO_SID,creds.TWILIO_AUTH_TOKEN)
    for article in formatted_article:
        message = client.messages.create(

        body= article,
        from_= creds.VERIFIED_TWILIO_NUMBER,
        to = creds.MY_NUMBER

)