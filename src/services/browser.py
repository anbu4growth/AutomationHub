"""
Browser Service
"""

from playwright.sync_api import sync_playwright
from src.config.settings import HEADLESS, SLOW_MO


class BrowserService:

    def __init__(self):

        self.playwright = sync_playwright().start()

        self.browser = self.playwright.chromium.launch(
            headless=HEADLESS,
            slow_mo=SLOW_MO
        )

        self.context = self.browser.new_context(
            viewport={
                "width": 1440,
                "height": 900
            }
        )

        self.page = self.context.new_page()

    def close(self):

        self.context.close()
        self.browser.close()
        self.playwright.stop()