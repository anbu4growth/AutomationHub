"""
TechnoFunda Follow Back Module
"""

from playwright.sync_api import Page


def click_follow_back(page: Page):

    selector = "div[role='button']:has(svg.icon-tabler-user-plus)"

    buttons = page.locator(selector)

    count = buttons.count()

    print(f"\nBlue Follow Buttons : {count}")

    clicked = 0

    for i in range(count):

        try:

            print(f"Clicking {i+1}/{count}")

            buttons.nth(i).click()

            page.wait_for_timeout(1500)

            clicked += 1

        except Exception as ex:

            print(ex)

    return clicked


def previous_page(page: Page):

    previous = page.locator(
        "button[aria-label='Go to previous page']"
    )

    if previous.count() == 0:

        return False

    if previous.is_disabled():

        return False

    previous.click()

    page.wait_for_load_state("networkidle")

    page.wait_for_timeout(1000)

    return True