from datetime import datetime

from src.google_sheets.sheets import get_logs_sheet

sheet = get_logs_sheet()

sheet.append_row([
    datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "SYSTEM",
    "SUCCESS",
    "Automation Hub Initialized"
])

print("Google Sheets Connected Successfully.")