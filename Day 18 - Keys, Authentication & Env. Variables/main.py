import requests
import os
from twilio.rest import Client

api_key = "bf8aadda859ac981b75dce4c4f5fbc28"
OWM_Endpoint = "https://api.openweathermap.org/data/3.0/onecall?"
my_lat = 48.148598
my_long = 17.107748

account_sid = os.environ['ACe54ad10f483695239ed84f33285dd064']
auth_token = os.environ['cd9166ad20c607d58c859ceb2c79ae38']

parameters = {
    "lat": my_lat,
    "lon": my_long,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

will_rain = False

response = requests.get(OWM_Endpoint, params=parameters, verify=False)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]["weather"][0]["id"]
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain. Don't forget to bring an Umbrella!",
        from_='+19895752051',
        to='+421902899334'
    )

    print(message.sid)
