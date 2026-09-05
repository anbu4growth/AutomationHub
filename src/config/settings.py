"""
Application Settings
Loads all configuration from .env
"""

import os
from dotenv import load_dotenv

load_dotenv()

# -----------------------------
# TechnoFunda Credentials
# -----------------------------

TF_USERNAME = os.getenv("TF_USERNAME")
TF_PASSWORD = os.getenv("TF_PASSWORD")

# -----------------------------
# URLs
# -----------------------------

TF_BASE_URL = "https://app.technofundainvesting.com"

# -----------------------------
# Browser
# -----------------------------

HEADLESS = True
SLOW_MO = 500

# -----------------------------
# Google Sheets
# -----------------------------

GOOGLE_SHEET_ID = os.getenv("GOOGLE_SHEET_ID")
GOOGLE_CREDENTIALS = os.getenv("GOOGLE_CREDENTIALS")