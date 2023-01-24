import requests
import os
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

api_key = "WTNC6T5EENV34V17"
news_api_key = "5b80b7092d1a4f97a0a38e21cfb51082"

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": api_key
}

news_parameters = {
    "q": STOCK,
    "apiKey": news_api_key
}

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

account_sid = os.environ['TWILIO_ACCOUNT_SID'] = "ACe54ad10f483695239ed84f33285dd064"
auth_token = os.environ['TWILIO_AUTH_TOKEN'] = "cd9166ad20c607d58c859ceb2c79ae38"
client = Client(account_sid, auth_token)


response = requests.get(STOCK_ENDPOINT, params=parameters)
news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)

data = response.json()
news_data = news_response.json()

daily_data = data["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]

yesterday_closing_price = data_list[1]["2022-08-12"]["4. close"]
day_before_yesterday_closing_price = data_list[1]["2022-08-11"]["4. close"]


difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
diff_percent = (difference/float(yesterday_closing_price)) * 100

articles = news_data["articles"]
three_articles = articles[:3]
print(three_articles)


if diff_percent > 4:
    for i in range(len(three_articles)):
        message = client.messages \
            .create(
            body=f"{three_articles[i]['title']}\n{three_articles[i]['description']}",
            from_='+19895752051',
            to='+421902899334'
        )

        print(message.sid)


