"""
TechnoFunda Top 10 Trending Satellite WL Collector
"""

from datetime import datetime
from zoneinfo import ZoneInfo

from playwright.sync_api import Page

from src.services.logger import logger
from src.services.google_sheets import google_sheets


class SatelliteCollector:

    def __init__(self, page: Page):

        self.page = page
        self.timezone = ZoneInfo("Asia/Kolkata")

    # =====================================================
    # Collect
    # =====================================================

    def collect(self):

        logger.start("Satellite Watchlist")

        stocks = []

        now = datetime.now(self.timezone)

        card = (
            self.page
            .locator(
                "h4:text('Top 10 Trending Satellite WL')"
            )
            .locator(
                "xpath=ancestor::div[contains(@class,'MuiCard-root')]"
            )
        )

        bodies = card.locator("table tbody")

        logger.info(f"Rows Found : {bodies.count()}")

        for i in range(bodies.count()):

            body = bodies.nth(i)

            try:

                row = body.locator("tr").first

                cols = row.locator("td")

                if cols.count() < 4:
                    continue

                symbol = (
                    cols.nth(0)
                    .locator("b")
                    .inner_text()
                    .strip()
                )

                tradingview = ""
                screener = ""

                links = cols.nth(1).locator("a")

                for j in range(links.count()):

                    href = links.nth(j).get_attribute("href")

                    if not href:
                        continue

                    href_lower = href.lower()

                    if "tradingview" in href_lower:
                        tradingview = href

                    elif "screener" in href_lower:
                        screener = href

                wc = cols.nth(2).inner_text().strip()

                yc = cols.nth(3).inner_text().strip()

                stocks.append({

                    "date": now.strftime("%d-%b-%Y"),

                    "rank": i + 1,

                    "symbol": symbol,

                    "company": "",

                    "wc": wc,

                    "yc": yc,

                    "tradingview": tradingview,

                    "screener": screener

                })

            except Exception as ex:

                logger.exception(ex)

        logger.line()

        rows = []

        for stock in stocks:

            logger.info(
                f"{stock['rank']:>2}. "
                f"{stock['symbol']:<12} "
                f"WC={stock['wc']:<5} "
                f"YC={stock['yc']}"
            )

            rows.append([
                stock["date"],
                stock["rank"],
                stock["symbol"],
                stock["company"],
                stock["wc"],
                stock["yc"],
                stock["tradingview"],
                stock["screener"]
            ])

        logger.line()

        google_sheets.append_rows(
            "SatelliteWL",
            rows
        )

        logger.finish("Satellite Watchlist")

        return stocks


# =====================================================
# Entry Point
# =====================================================

def collect_satellite(page: Page):

    collector = SatelliteCollector(page)

    return collector.collect()