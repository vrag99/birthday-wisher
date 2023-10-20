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
