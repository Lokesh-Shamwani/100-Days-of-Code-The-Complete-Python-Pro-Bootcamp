import requests
from pprint import pprint
from flight_data import FlightData
from dotenv import load_dotenv
import os


def configure():
    load_dotenv()


configure()


tequila_endpoint = "https://tequila-api.kiwi.com"
tequila_apikey = os.getenv("tequila_apikey")


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        pass

    def get_destination_code(self, city_name):
        HEADERS = {"apikey": tequila_apikey}
        QUERY = {"term": city_name, "location_types": "city"}

        response = requests.get(
            url=f"{tequila_endpoint}/locations/query",
            headers=HEADERS,
            params=QUERY,
        )
        results = response.json()["locations"]
        code = results[0]["code"]
        return code

    def check_flights(
        self, origin_city_code, destination_city_code, from_time, to_time
    ):
        headers = {"apikey": tequila_apikey}
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time,
            "date_to": to_time,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP",
        }
        response = requests.get(
            url=f"{tequila_endpoint}/v2/search", headers=headers, params=query
        )

        try:
            data = response.json()["data"][0]
        except IndexError:
            query["max_stopovers"] = 1
            response = requests.get(
                url=f"{tequila_endpoint}/v2/search",
                headers=headers,
                params=query,
            )
            try:
                data = response.json()["data"][0]
                pprint(data)
            except IndexError:
                return None
            else:
                FD = FlightData(
                    price=data["price"],
                    origin_city=data["route"][0]["cityFrom"],
                    origin_airport=data["route"][0]["flyFrom"],
                    destination_city=data["route"][1]["cityTo"],
                    destination_airport=data["route"][1]["flyTo"],
                    out_date=data["route"][0]["local_departure"].split("T")[0],
                    return_date=data["route"][2]["local_departure"].split("T")[0],
                    stop_overs=1,
                    via_city=data["route"][0]["cityTo"],
                )
                print(f"{FD.destination_city}: £{FD.price}")
                return FD

        else:
            FD = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0],
            )
            print(f"{FD.destination_city}: £{FD.price}")
            return FD
