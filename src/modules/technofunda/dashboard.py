"""
TechnoFunda Dashboard Collector
"""

import re

from datetime import datetime
from zoneinfo import ZoneInfo

from playwright.sync_api import Page

from src.services.logger import logger
from src.services.google_sheets import google_sheets


class DashboardCollector:

    def __init__(self, page: Page):

        self.page = page
        self.timezone = ZoneInfo("Asia/Kolkata")

    # =====================================================
    # Helpers
    # =====================================================

    def _extract_number(self, text: str):

        if not text:
            return ""

        m = re.search(
            r"[-+]?\d*\.?\d+",
            text.replace(",", "")
        )

        return m.group() if m else ""

    def _read_metric(self, title: str):

        cards = self.page.locator(".MuiCard-root")

        for i in range(cards.count()):

            card = cards.nth(i)

            try:

                heading = (
                    card.locator("h5")
                    .inner_text()
                    .strip()
                    .upper()
                )

            except Exception:
                continue

            if heading == title.upper():

                value = (
                    card.locator("h3")
                    .inner_text()
                    .strip()
                )

                return self._extract_number(value)

        return ""

    # =====================================================
    # Collect
    # =====================================================

    def collect(self):

        logger.start("Dashboard")

        now = datetime.now(self.timezone)

        data = {

            "date": now.strftime("%d-%b-%Y"),

            "time": now.strftime("%H:%M:%S"),

            "core_audit": self._read_metric(
                "CORE AUDIT"
            ),

            "events": self._read_metric(
                "EVENTS"
            ),

            "ideas": self._read_metric(
                "IDEAS"
            ),

            "rewards": self._read_metric(
                "REWARDS"
            )
        }

        logger.info(
            f"Core Audit : {data['core_audit']}"
        )

        logger.info(
            f"Events      : {data['events']}"
        )

        logger.info(
            f"Ideas       : {data['ideas']}"
        )

        logger.info(
            f"Rewards     : {data['rewards']}"
        )

        google_sheets.append_row(
    "Dashboard",
    [
        data["date"],
        data["time"],
        data["core_audit"],
        data["events"],
        data["ideas"],
        data["rewards"]
    ]
)

        logger.finish("Dashboard")

        return data


# =====================================================
# Entry Point
# =====================================================

def collect_dashboard(page: Page):

    collector = DashboardCollector(page)

    return collector.collect()