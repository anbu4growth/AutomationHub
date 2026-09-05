"""
TechnoFunda Login Module
"""

from playwright.sync_api import Page

from src.config.settings import (
    TF_BASE_URL,
    TF_USERNAME,
    TF_PASSWORD
)


def login(page: Page):

    print("Opening TechnoFunda...")

    page.goto(
        TF_BASE_URL,
        wait_until="networkidle"
    )

    print("Logging in...")

    page.get_by_role(
        "textbox",
        name="Email / Mobile"
    ).fill(TF_USERNAME)

    page.get_by_role(
        "textbox",
        name="Password"
    ).fill(TF_PASSWORD)

    page.get_by_role(
        "button",
        name="Login",
        exact=True
    ).click()

    page.wait_for_load_state("networkidle")

    print("Login Successful")