import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 48.148598
MY_LONG = 17.107748

MY_EMAIL = "krsak.danko@yahoo.com"
MY_PASSWORD = "gufaqqogyijfnlsv"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters, verify=False)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now().hour


def check_location(lat, long, iss_lat, iss_long):
    if ((lat + 5) >= iss_lat >= (lat-5)) and ((long + 5) >= iss_long >= (long-5)):
        return True
    else:
        return False


while True:
    time.sleep(60)
    if check_location(MY_LAT, MY_LONG, iss_latitude, iss_longitude) and (sunset <= time_now <= sunrise):
        with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg="Subject: Look Up!\n\nRead Subject.")
