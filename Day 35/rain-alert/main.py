import requests
import smtplib
from dotenv import load_dotenv
import os


def configure():
    load_dotenv()


configure()


MY_EMAIL = os.getenv("email")
MY_PASSWORD = os.getenv("app_password")

OWM_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"


parameters = {
    "lat": 43.278290,
    "lon": -75.571760,
    "exclude": "current,minutely,daily",
    "appid": os.getenv("api_key"),
}

response = requests.get(url=OWM_Endpoint, params=parameters)
response.raise_for_status()
data = response.json()


will_rain = False
for i in range(0, 12):
    weather_condition_code = data["hourly"][i]["weather"][0]["id"]
    if int(weather_condition_code) < 700:
        will_rain = True

if will_rain:
    with smtplib.SMTP(host="smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Testing Project RAIN ALERT\n\nIt's gonna rain today, Bring an Umbrella",
        )
