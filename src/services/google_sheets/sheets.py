"""
Google Sheets Service

Worksheets

1. Dashboard
2. TrendingSector
3. SatelliteWL
4. Logs
"""

import os
import json
import gspread

from dotenv import load_dotenv
from google.oauth2.service_account import Credentials

load_dotenv()

print("=" * 60)
print("GOOGLE SHEETS SERVICE V2 LOADED")
print("=" * 60)

print("Credentials Preview:", os.getenv("GOOGLE_CREDENTIALS")[:20])

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]


# =====================================================
# Authentication
# =====================================================

credentials_value = os.getenv("GOOGLE_CREDENTIALS")

if not credentials_value:
    raise RuntimeError("GOOGLE_CREDENTIALS environment variable not found.")

print("=" * 60)
print("Google Credentials Loaded")
print("Starts With :", repr(credentials_value[:30]))
print("=" * 60)

# Local Development (.env points to JSON file)
if os.path.isfile(credentials_value):

    print("Authentication Mode : Service Account File")

    creds = Credentials.from_service_account_file(
        credentials_value,
        scopes=SCOPES
    )

# Cloud Run (Secret Manager contains JSON)
else:

    print("Authentication Mode : Service Account JSON")

    creds = Credentials.from_service_account_info(
        json.loads(credentials_value),
        scopes=SCOPES
    )

client = gspread.authorize(creds)

spreadsheet = client.open_by_key(
    os.getenv("GOOGLE_SHEET_ID")
)


# =====================================================
# Worksheet Helpers
# =====================================================

def get_dashboard_sheet():
    return spreadsheet.worksheet("Dashboard")


def get_trending_sheet():
    return spreadsheet.worksheet("TrendingSector")


def get_satellite_sheet():
    return spreadsheet.worksheet("SatelliteWL")


def get_logs_sheet():
    return spreadsheet.worksheet("Logs")


# =====================================================
# Dashboard
# =====================================================

def append_dashboard(data):

    sheet = get_dashboard_sheet()

    sheet.append_row([
        data["date"],
        data["time"],
        data["core_audit"],
        data["events"],
        data["ideas"],
        data["rewards"]
    ])

    print("✓ Dashboard uploaded.")


# =====================================================
# Trending Sector
# =====================================================

def append_trending(rows):

    sheet = get_trending_sheet()

    for row in rows:

        sheet.append_row([
            row["date"],
            row["rank"],
            row["sector"],
            row["wc"],
            row["yc"]
        ])

    print("✓ Trending Sector uploaded.")


# =====================================================
# Satellite Watchlist
# =====================================================

def append_satellite(rows):

    sheet = get_satellite_sheet()

    for row in rows:

        sheet.append_row([
            row["date"],
            row["rank"],
            row["symbol"],
            row["company"],
            row["wc"],
            row["yc"],
            row["tradingview"],
            row["screener"]
        ])

    print("✓ Satellite Watchlist uploaded.")


# =====================================================
# Logs
# =====================================================

def write_log(status, module, remarks=""):

    from datetime import datetime

    sheet = get_logs_sheet()

    now = datetime.now()

    sheet.append_row([
        now.strftime("%d-%b-%Y"),
        now.strftime("%H:%M:%S"),
        status,
        module,
        remarks
    ])

    print(f"LOG [{status}] {module}")


# =====================================================
# Test
# =====================================================

if __name__ == "__main__":

    print("Google Sheets Connected Successfully")

    print("Dashboard Sheet :", get_dashboard_sheet().title)
    print("Trending Sheet  :", get_trending_sheet().title)
    print("Satellite Sheet :", get_satellite_sheet().title)
    print("Logs Sheet      :", get_logs_sheet().title)