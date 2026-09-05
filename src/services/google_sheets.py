"""
AutomationHub Google Sheets Service
"""

import json
import os

import gspread
from google.oauth2.service_account import Credentials

from src.config.settings import (
    GOOGLE_CREDENTIALS,
    GOOGLE_SHEET_ID,
)

from src.services.logger import logger


SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]


class GoogleSheetsService:

    def __init__(self):

        self.client = None
        self.spreadsheet = None
        self.connected = False
        self._worksheets = {}

    # =====================================================
    # Connect
    # =====================================================

    def connect(self):

        if self.connected:
            return

        logger.info("Connecting to Google Sheets...")

        if not GOOGLE_CREDENTIALS:
            raise RuntimeError("GOOGLE_CREDENTIALS is empty.")

        # Local JSON file
        if os.path.isfile(GOOGLE_CREDENTIALS):

            logger.info("Using Service Account File")

            creds = Credentials.from_service_account_file(
                GOOGLE_CREDENTIALS,
                scopes=SCOPES,
            )

        # Cloud Run Secret
        else:

            logger.info("Using Secret Manager JSON")

            creds = Credentials.from_service_account_info(
                json.loads(GOOGLE_CREDENTIALS),
                scopes=SCOPES,
            )

        self.client = gspread.authorize(creds)

        self.spreadsheet = self.client.open_by_key(
            GOOGLE_SHEET_ID
        )

        self.connected = True

        logger.success("Google Sheets Connected.")

    # =====================================================
    # Worksheet
    # =====================================================

    def worksheet(self, name):

        self.connect()

        if name not in self._worksheets:

            logger.info(f"Opening worksheet : {name}")

            self._worksheets[name] = (
                self.spreadsheet.worksheet(name)
            )

        return self._worksheets[name]

    # =====================================================
    # Append Single Row
    # =====================================================

    def append_row(self, worksheet_name, row):

        logger.info(
            f"Appending row to {worksheet_name}"
        )

        logger.info(str(row))

        sheet = self.worksheet(worksheet_name)

        sheet.append_row(
            row,
            value_input_option="USER_ENTERED",
        )

        logger.success(
            f"{worksheet_name} updated."
        )

    # =====================================================
    # Append Multiple Rows
    # =====================================================

    def append_rows(self, worksheet_name, rows):

        if not rows:
            return

        logger.info(
            f"Appending {len(rows)} rows to {worksheet_name}"
        )

        sheet = self.worksheet(worksheet_name)

        sheet.append_rows(
            rows,
            value_input_option="USER_ENTERED",
        )

        logger.success(
            f"{worksheet_name} updated."
        )

    # =====================================================
    # Logs
    # =====================================================

    def write_log(
        self,
        status,
        module,
        remarks=""
    ):

        from datetime import datetime
        from zoneinfo import ZoneInfo

        now = datetime.now(
            ZoneInfo("Asia/Kolkata")
        )

        self.append_row(
            "Logs",
            [
                now.strftime("%d-%b-%Y"),
                now.strftime("%H:%M:%S"),
                status,
                module,
                remarks,
            ],
        )


google_sheets = GoogleSheetsService()


if __name__ == "__main__":

    logger.banner()

    google_sheets.connect()

    google_sheets.append_row(
        "Dashboard",
        [
            "TEST",
            "18:45",
            100,
            200,
            300,
            99.99,
        ],
    )

    logger.success("Test completed.")