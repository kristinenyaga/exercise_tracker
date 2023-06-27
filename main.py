import requests
import os
from dotenv import dotenv_values
from datetime import datetime as dt

env_vars = dotenv_values('.env')
APP_ID = env_vars['APP_ID']
API_KEY = env_vars['API_KEY']
TOKEN = env_vars['TOKEN']
URL = env_vars['URL']

exercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'


input_data = input("Tell me which exercises you did? ")
headers={
    "Content-Type": "application/json",
    "x-app-key":API_KEY,
    "x-app-id":APP_ID
}

exercise_data={
    "query":input_data,
    "gender":"female",
    "weight_kg":62,
    "height_cm":167.64,
    "age":20
}

datetime_obj = dt.now()

date = datetime_obj.date().isoformat()
time = datetime_obj.time().isoformat()
response=requests.post(url=exercise_endpoint,headers=headers,json=exercise_data)
data=response.json()['exercises']

for exercise in data:
  
    body={
        "workout": {
            "date": date,
         	  "time": time,
            "exercise": exercise['name'].title(),
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories']
        }
    }
    headers = {"Authorization": f"Bearer {TOKEN}"}
    response=requests.post(url=URL,json=body,headers=headers)
    print(response.json())


