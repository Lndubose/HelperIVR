# Welcome to the Helper Bee IVR for Helpers
To start the application, you will need to clone the project as well as have
Flask, Python, and Twilio. Additionally, you will need a [twilio account](https://www.twilio.com/). This 
project will work on the free account, but be aware that recording and transcribing
does have a fee.

To download Python you can go [here](https://docs.python.org/3/using/index.html).

[Here](https://docs.python-guide.org/starting/install3/win/) is a good resource for window users to download python.

You will also need to have pip installed.

For Flask, here is the [installation page](http://flask.pocoo.org/docs/0.12/installation/#installation).

To run your webhooks locally, [ngrok](https://www.twilio.com/blog/2013/10/test-your-webhooks-locally-with-ngrok.html) is a good tool. I recommend reading this before starting the program because it shows were the urls are placed in the twilio app.


## Now to the project:
- Clone the repo into your perferred text editor
- You will want to setup a virtualenv to install Flask, dotenv, and twilio
    - Flask will be `pip install Flask`
    - Dotenv will be `pip install -U python-dotenv`
    - Twilio is `pip install twilio`
- You will need a twilio phone number. [Here](https://www.twilio.com/docs/voice/quickstart/python) is the page to show you how.
- You will need a .env file that will hold:
```
TWILIO_ACCOUNT_SID="Account SID from twilio"
TWILIO_AUTH_TOKEN="Authentication token"
REPRESENTATIVE_NUMBER="Phone number here"
TWILIO_NUMBER="Number you get from twilio"
```
- Now start your localhost machine (this is where ngrok is used). You need to enter the url for a call comes in at your active phone numbers.
- After that is done, run the program: `python __init.py__`
- Now call the number that you have as your TWILIO_NUMBER in your env and the program should run.

## Additional resources:
- [Twilio docs](https://www.twilio.com/docs/)
- [Flask docs](http://flask.pocoo.org/docs/0.12/)
- [Python docs](https://docs.python.org/3/)
- [Python dotenv](https://github.com/theskumar/python-dotenv#installation)
