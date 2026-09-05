"""
TechnoFunda Logout
"""

from playwright.sync_api import Page


def logout(page: Page):

    page.get_by_role("button").last.click()

    page.get_by_text("Logout").click()

    page.wait_for_load_state("networkidle")