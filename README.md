### 📈 Stock Price Monitor

This project monitors stock price changes and sends news alerts if significant changes are detected. It uses the Alpha Vantage API for stock prices, the News API for fetching news articles, and the Twilio API for sending SMS notifications.

#### 🛠️ Requirements

- **Python 3**
- **Requests library**: `pip install requests`
- **Twilio library**: `pip install twilio`

#### ⚙️ Setup

1. **Alpha Vantage API Key**: Sign up at [Alpha Vantage](https://www.alphavantage.co/) to get your API key.
2. **News API Key**: Sign up at [News API](https://newsapi.org/) to get your API key.
3. **Twilio Account**: Sign up at [Twilio](https://www.twilio.com/) to get your account SID, auth token, and phone number.

#### 📄 Configuration

Create a `config.py` file with the following content:
```python
ALPHA_VANTAGE_API_KEY = 'your_alpha_vantage_api_key'
NEWS_API_KEY = 'your_news_api_key'
TWILIO_ACCOUNT_SID = 'your_twilio_account_sid'
TWILIO_AUTH_TOKEN = 'your_twilio_auth_token'
TWILIO_PHONE_NUMBER = 'your_twilio_phone_number'
TO_PHONE_NUMBER = 'your_phone_number'
COMPANY_NAME = 'your_company_name'
STOCK_SYMBOL = 'your_stock_symbol'
```

#### 📋 Steps

**STEP 1: Stock Price Monitoring**

1. **Get Yesterday's Closing Stock Price:**
    - Use the Alpha Vantage API to get the daily stock prices.
    - Extract the closing price for yesterday.

2. **Get Day Before Yesterday's Closing Stock Price:**
    - Extract the closing price for the day before yesterday.

3. **Calculate the Difference:**
    - Find the positive difference between the two closing prices.

4. **Calculate the Percentage Difference:**
    - Calculate the percentage difference between the two closing prices.

5. **Check for Significant Change:**
    - If the percentage difference is greater than 5%, proceed to get news.

**STEP 2: Fetch News Articles**

1. **Get News Articles:**
    - Use the News API to get the latest news articles related to the company.

2. **Select Top 3 Articles:**
    - Use Python's slice operator to get the first 3 articles.

**STEP 3: Send SMS Notifications**

1. **Prepare Messages:**
    - Create a list of messages with the article headlines and descriptions.

2. **Send Messages via Twilio:**
    - Use the Twilio API to send each article as a separate SMS message.

---

This Stock Price Monitor is a fun and easy way to stay on top of your investments. With real-time stock monitoring, news alerts, and SMS notifications, you'll never miss a beat! 📲🚀