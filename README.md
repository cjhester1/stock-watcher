##Stock Watcher### 

Flow Chart of program

#1. - Get yesterday's closing stock price. I used list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

#2. - Get the day before yesterday's closing stock price

#3. - Find the positive difference between 1 (yesterday) and 2 (day before yesterday).

#4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

#5. -  TEST --> If percent difference is greater than 5 then print("Get News").

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#8. - Create a new list of the first 3 article's headline and description using list comprehension.

#9. - Send each article as a separate message via Twilio. 