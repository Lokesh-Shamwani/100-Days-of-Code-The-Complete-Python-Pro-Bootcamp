import requests
from datetime import datetime
from dotenv import load_dotenv
import os


def configure():
    load_dotenv()


configure()

APP_ID = os.getenv("APP_ID")
NUTRITIONIX_API_KEY = os.getenv("NUTRITIONIX_API_KEY")
nutritionix_endpoint = "https://trackapi.nutritionix.com"

sheety_endpoint = "https://api.sheety.co"
SHEETY_API = os.getenv("SHEETY_API")
WORKSHEET = f"{sheety_endpoint}/{SHEETY_API}/workoutTracking/workouts"
SHEETY_USERNAME = os.getenv("SHEETY_USERNAME")
SHEETY_PASSWORD = os.getenv("SHEETY_PASSWORD")


GENDER = "male"
WEIGHT = 66
HEIGHT_CM = 155
AGE = 21

headers = {
    "x-app-id": APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
    "x-remote-user-id": "0",
}
exercise_endpoint = f"{nutritionix_endpoint}/v2/natural/exercise"

excercise_text = input("Tell me which excercise you did: ")
exercise_config = {
    "query": excercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}
response = requests.post(url=exercise_endpoint, json=exercise_config, headers=headers)
result = response.json()
exercises = result["exercises"]
print(exercises)

current_date = datetime.now().strftime("%d/%m/%Y")
current_time = datetime.now().strftime("%X")

for exercise in exercises:
    sheet_inputs = {
        "workout": {
            "date": current_date,
            "time": current_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    sheet_response = requests.post(
        url=WORKSHEET, json=sheet_inputs, auth=(SHEETY_USERNAME, SHEETY_PASSWORD)
    )
    print(sheet_response.text)
