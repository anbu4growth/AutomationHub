import re
from playwright.sync_api import Page


def open_followers(page: Page):

    print("Opening My Profile...")

    page.get_by_role("button", name="My Profile").click()

    page.wait_for_timeout(1000)

    print("Opening Followers...")

    page.get_by_text("Followers").click()

    page.wait_for_load_state("networkidle")


def goto_last_page(page: Page):

    print("Finding last page...")

    buttons = page.locator("button")

    highest = 1

    for i in range(buttons.count()):

        btn = buttons.nth(i)

        aria = btn.get_attribute("aria-label") or ""

        m = re.search(r"(\d+)", aria)

        if m:

            highest = max(highest, int(m.group(1)))

    print(f"Highest Page Found : {highest}")

    if highest > 1:

        page.get_by_role(
            "button",
            name=f"Go to page {highest}"
        ).click()

        page.wait_for_load_state("networkidle")

    return highest