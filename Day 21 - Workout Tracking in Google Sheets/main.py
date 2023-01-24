import requests
import datetime as dt

date = dt.datetime.now().strftime("%d/%m/%Y")
time = dt.datetime.now().strftime("%X")

API_KEY = "6ff73cf7e3fa07bb7dc3e230c1f05cc0"
API_ID = "af883e95"
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = "https://api.sheety.co/d24509387f4b983146c5f3e52e1bb325/copyOfMyWorkouts/workouts"
exercise_text = input("Tell me which exercise you did? ")


headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0"
}

params = {
    "query": exercise_text,
    "gender": "male",
    "weight_kg": 84,
    "height_cm": 185,
    "age": 25
}


response = requests.post(url=NUTRITIONIX_ENDPOINT, json=params, headers=headers)
print(response.json()["exercises"][0])
exercise = response.json()["exercises"][0]["name"]
duration = response.json()["exercises"][0]["duration_min"]
calories = response.json()["exercises"][0]["nf_calories"]

sheety_params = {
    "workout": {
        "date": date,
        "time": time,
        "exercise": exercise.title(),
        "duration": duration,
        "calories": calories

    }
}

sheety_headers = {
    "Authorization": "Bearer a[oshin[1tnfg[apegm'anpisn"
}

sheety_response = requests.post(url=SHEETY_ENDPOINT, json=sheety_params, headers=sheety_headers)


