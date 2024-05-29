import requests
from dotenv import load_dotenv
import os


def configure():
    load_dotenv()


configure()

worksheet_endpoint = f"https://api.sheety.co/{os.getenv('worksheet_api')}/myFlightDeals"

print("Welcome to Angela's Flight Club.\nWe find the best flight deals and email you.")

first_name = input("What is your first name?\n")
last_name = input("What is your last name?\n")
email = input("What is your email? \n")
email_again = input("Type you email again.\n")
if email == email_again:
    user_data = {
        "user": {
            "firstName": first_name,
            "lastName": last_name,
            "email": email,
        }
    }
    response = requests.post(url=f"{worksheet_endpoint}/users", json=user_data)
    if response.status_code == 200:
        print("You're in the club!")
    else:
        print("email doesn't match")
