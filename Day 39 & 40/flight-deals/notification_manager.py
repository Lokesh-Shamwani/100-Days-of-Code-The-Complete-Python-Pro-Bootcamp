import smtplib
import requests
from pprint import pprint
from dotenv import load_dotenv
import os


def configure():
    load_dotenv()


configure()


MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")

WORKSHEET_ENDPOINT = f"https://api.sheety.co/{os.getenv('worksheet_api')}/myFlightDeals"


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self) -> None:
        self.data = requests.get(url=f"{WORKSHEET_ENDPOINT}/users")
        self.users = self.data.json()["users"]

    def send_mails(self, message):
        with smtplib.SMTP(host="smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            for user in self.users:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=user["email"],
                    msg=message,
                )


notification_manager = NotificationManager()
