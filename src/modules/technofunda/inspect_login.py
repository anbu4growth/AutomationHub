from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page(viewport={"width": 1440, "height": 900})

    page.goto("https://app.technofundainvesting.com", wait_until="networkidle")

    print("\n=== INPUT FIELDS ===")

    inputs = page.locator("input")

    for i in range(inputs.count()):
        e = inputs.nth(i)

        print("----------------------------")
        print("Type :", e.get_attribute("type"))
        print("Name :", e.get_attribute("name"))
        print("ID   :", e.get_attribute("id"))
        print("Placeholder :", e.get_attribute("placeholder"))

    print("\n=== BUTTONS ===")

    buttons = page.locator("button")

    for i in range(buttons.count()):
        print(buttons.nth(i).inner_text())

    input("\nPress ENTER to close...")

    browser.close()