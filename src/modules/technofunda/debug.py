from playwright.sync_api import Page

def inspect_cards(page: Page):

    cards = page.locator(".MuiPaper-root")

    print(f"Cards : {cards.count()}")

    for i in range(cards.count()):

        card = cards.nth(i)

        print("=" * 60)

        print(card.inner_text())

        print(card.locator("svg").count())