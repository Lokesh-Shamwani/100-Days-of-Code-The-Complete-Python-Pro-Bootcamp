import requests
import smtplib
from dotenv import load_dotenv
import os


def configure():
    load_dotenv()


configure()

MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = os.getenv("STOCK_API_KEY")
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "outputsize": "compact",
    "apikey": STOCK_API_KEY,
}

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
news_parameters = {
    "qInTitle": COMPANY_NAME,
    "apiKey": NEWS_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
data = response.json()["Time Series (Daily)"]

data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = float(yesterday_data["4. close"])

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = float(day_before_yesterday_data["4. close"])

difference = round(yesterday_closing_price - day_before_yesterday_closing_price, 2)
up_down = None
if difference > 0:
    up_down = "⬆️"
else:
    up_down = "⬇️"

avg_value = (yesterday_closing_price + day_before_yesterday_closing_price) / 2
diff_percent = round((difference / avg_value) * 100, 2)

if abs(diff_percent) > 1:
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
    articles = news_response.json()["articles"]

    first_three_articles = articles[:3]


    with smtplib.SMTP(host="smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        for article in first_three_articles:
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"SUBJECT: TESTING STOCK NEW PROJECT\n\n{STOCK_NAME}: {diff_percent}%\nHeadline: {article['title']}.\n\n{article['description']}".encode(
                    "utf-8"
                ),
            )
