import os
import gspread
from dotenv import load_dotenv
from google.oauth2.service_account import Credentials

load_dotenv()

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

creds = Credentials.from_service_account_file(
    os.getenv("GOOGLE_CREDENTIALS"),
    scopes=SCOPES
)

client = gspread.authorize(creds)

spreadsheet = client.open_by_key(
    os.getenv("GOOGLE_SHEET_ID")
)

def get_logs_sheet():
    return spreadsheet.worksheet("Logs")