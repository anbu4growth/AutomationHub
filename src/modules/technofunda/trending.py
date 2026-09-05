"""
TechnoFunda Trending Sector Collector
"""

from datetime import datetime
from zoneinfo import ZoneInfo

from playwright.sync_api import Page

from src.services.logger import logger
from src.services.google_sheets import google_sheets


class TrendingCollector:

    def __init__(self, page: Page):

        self.page = page
        self.timezone = ZoneInfo("Asia/Kolkata")

    # =====================================================
    # Collect
    # =====================================================

    def collect(self):

        logger.start("Trending Sector")

        sectors = []

        now = datetime.now(self.timezone)

        card = (
            self.page
            .locator("h4:text('Top 5 Trending Sector')")
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

                if cols.count() < 3:
                    continue

                sector = (
                    cols.nth(0)
                    .locator("h6")
                    .inner_text()
                    .strip()
                )

                wc = cols.nth(1).inner_text().strip()

                yc = cols.nth(2).inner_text().strip()

                sectors.append({

                    "date": now.strftime("%d-%b-%Y"),

                    "rank": i + 1,

                    "sector": sector,

                    "wc": wc,

                    "yc": yc

                })

            except Exception as ex:

                logger.exception(ex)

        logger.line()

        rows = []

        for s in sectors:

            logger.info(
                f"{s['rank']}. "
                f"{s['sector']} | "
                f"WC={s['wc']} | "
                f"YC={s['yc']}"
            )

            rows.append([
                s["date"],
                s["rank"],
                s["sector"],
                s["wc"],
                s["yc"]
            ])

        logger.line()

        google_sheets.append_rows(
            "TrendingSector",
            rows
        )

        logger.finish("Trending Sector")

        return sectors


# =====================================================
# Entry Point
# =====================================================

def collect_trending(page: Page):

    collector = TrendingCollector(page)

    return collector.collect()