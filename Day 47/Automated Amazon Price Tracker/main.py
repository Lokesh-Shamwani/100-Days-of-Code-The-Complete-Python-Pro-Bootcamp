import lxml
import requests
from bs4 import BeautifulSoup
import smtplib
from dotenv import load_dotenv
import os


def configure():
    load_dotenv()


configure()


MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")

my_browser_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,ur;q=0.8",
}

PRODUCT_URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
TARGET_PRICE = 85

response = requests.get(url=PRODUCT_URL, headers=my_browser_headers)
product_webpage = response.text

soup_product_page = BeautifulSoup(markup=product_webpage, features="lxml")
product_title = soup_product_page.title.text
price_span = soup_product_page.find("span", class_="a-offscreen")
product_price = float(price_span.getText().split("$")[1])
if product_price < TARGET_PRICE:
    message = (
        f"SUBJECT:Amazon Price Alert!\n\n{product_title} is now ${product_price}\n{PRODUCT_URL}"
    ).encode("utf-8")
    with smtplib.SMTP(
        host="smtp.gmail.com",
    ) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=message,
        )
