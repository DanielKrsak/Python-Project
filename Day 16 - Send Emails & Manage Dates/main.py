import smtplib
import datetime as dt
import random
import pandas as pd


MY_EMAIL = "krsak.danko@yahoo.com"
MY_PASSWORD = "rayoelfuklsjftmb"

today = dt.datetime.now()
today_tuple = today.day, today.month

data = pd.read_csv("birthdays.csv")
birthday_dict = {(value.month, value.day): value for key, value in data.iterrows()}
birthday_name = birthday_dict[today_tuple]["name"]


with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as file:
    data = file.read()
    data = data.replace("[NAME]", birthday_name)

if today_tuple in birthday_dict:
    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=MY_EMAIL,
                            msg=f"Subject: Happy Birthday\n\n{data}")

