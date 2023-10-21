# Boilerplate for bday-wish-automator
This is the starting point for the birthday wish automator.

## Setup
1. Download the zip file from above > extract it > open the folder in your preferred code editor.
2. Open your cmd(windows) or terminal (mac/linux/wsl) and run
    ```
    pip install virtualenv
    ```
3. **In the folder of the code, make a virtual environment** 
   ```
   virtualenv venv
   ```
4. Now, we'll activate out virtual environment.
   1. For windows: ```venv\Scripts\activate.bat```
   2. For literally any other OS: ```source venv/bin/activate```
5. Hey, you're almost there :)   
    Now, we'll install the python packages to get our code running.
    ```
    pip install -r requirements.txt
    ```
### And you're done with the setup!
---
## Get your `.env` setup.
1. Go to [App passwords](https://myaccount.google.com/apppasswords) > login into your mail
2. You'll see an input box for App Name. Make a new app with any name (say 'abcd') and copy the code that it gives and paste it into your .env file.
3. If it throws an error and says 'Go to your Google account'  
   - Enable 2 step verification on your account and enable less secure apps and try again.
   - If the error persists, try with another mail id.
---
## Make a birthday list
1. Go to your google sheets and make a document containing the names, emails and their birthdays.
2. Make a new project on [sheety](https://sheety.co) and paste your sheet url there and access your **API**.
---
**The solutions are there in the solutions folder.**

