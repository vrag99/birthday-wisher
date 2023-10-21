import os
from dotenv import load_dotenv

# Getting the environment variables
load_dotenv()
EMAIL = os.environ['EMAIL']
APP_PASSWORD = os.environ['APP_PASSWORD']

# Setting up the email sender
from redmail import EmailSender

# Email sender configuration using Google's smtp server.
email = EmailSender(
    host="smtp.gmail.com", 
    port=587,
    username=EMAIL,
    password=APP_PASSWORD
)

print("Succesfully setup the email sender :)")

# Code from here

import requests as r
import json
from datetime import date

# The URL you get from sheety
API_URL = ''

data = r.get(API_URL).json()
print(json.dumps(data, indent=2))

for person in data["sheet1"]:
    if person["date"] == date.today().strftime("%m/%d/%Y"):
        print(f"Today is {person['name']}'s birthday")
        email.send(
            subject = "Happy birthday!",
            sender = EMAIL,
            receivers= [person['email']],
            text = f"Happy birthday dear, {person['name']}"
        )
        print("mail sent successfully")