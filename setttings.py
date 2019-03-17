from dotenv import load_dotenv
import os

load_dotenv()
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
repNumber = os.getenv("PERSONAL_NUMBER")
