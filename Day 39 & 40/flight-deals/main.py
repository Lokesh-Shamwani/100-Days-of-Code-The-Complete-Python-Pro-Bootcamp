# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

ORIGIN_CITY_IATA = "LON"

DM = DataManager()
FS = FlightSearch()
notification_manager = NotificationManager()
sheet_data = DM.get_sheet_data()

for entry in sheet_data:
    if entry["iataCode"] == "":
        entry["iataCode"] = FS.get_destination_code(entry["city"])
        DM.destination_data = sheet_data
        DM.update_destination_codes()

tomorrow = (datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y")
six_months_from_today = (datetime.now() + timedelta(days=6 * 30)).strftime("%d/%m/%Y")

for destination in sheet_data:
    flight = FS.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_months_from_today,
    )

    if flight is None:
        continue

    if flight.price < destination["lowestPrice"]:
        message = f"Low price alert! Only GBP{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."

        if flight.stop_overs > 0:
            message += (
                f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."
            )
        notification_manager.send_mails(message=message)
