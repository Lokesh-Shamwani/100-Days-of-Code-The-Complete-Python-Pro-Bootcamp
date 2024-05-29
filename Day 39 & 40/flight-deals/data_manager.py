from pprint import pprint
import requests
from dotenv import load_dotenv
import os


def configure():
    load_dotenv()


configure()


WORKSHEET_ENDPOINT = (
    f"https://api.sheety.co/{os.getenv('worksheet_api')}/myFlightDeals"
)


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = []

    def get_sheet_data(self):
        self.response = requests.get(url=f"{WORKSHEET_ENDPOINT}/prices")
        print(self.response.status_code)
        self.destination_data = self.response.json()["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for entry in self.destination_data:
            new_data = {"price": {"iataCode": entry["iataCode"]}}
            requests.put(
                url=f"{WORKSHEET_ENDPOINT}/prices/{entry['id']}", json=new_data
            )
