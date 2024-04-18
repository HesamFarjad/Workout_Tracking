import requests
from datetime import datetime
import os

# GENDER = "YOUR GENDER"
# WEIGHT_KG = "YOUR WEIGHT"
# HEIGHT_CM = "YOUR HEIGHT"
# AGE = "YOUR AGE"

APP_ID = os.environ["NT_APP_ID"]
API_KEY = os.environ["NT_API_KEY"]

exercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
exercise_text = input("Tell me which exercises you did: ")


headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    # "gender": GENDER,
    # "weight_kg": WEIGHT_KG,
    # "height_cm": HEIGHT_CM,
    # "age": AGE
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(f"Result: {result}")

username = "29f54b553736565fc96db871106a11a1"
projectName = "workoutTracking"
sheetName = "workouts"
# sheet_endpoint = f"https://api.sheety.co/{username}/{projectName}/{sheetName}"
sheet_endpoint = os.environ["SHEET_ENDPOINT"]

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

bearer_headers = {
    "Authorization": f"Bearer {os.environ['TOKEN']}"
}

for i in result['exercises']:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": i["name"].title(),
            "duration": i["duration_min"],
            "calories": i["nf_calories"]
        }
    }

sheet_response = requests.post(url=sheet_endpoint, json=bearer_headers)
print(sheet_response.text)
