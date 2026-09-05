"""
Automation Hub
Main Entry Point
"""

import traceback

from src.services.browser import BrowserService
from src.modules.technofunda.runner import run


def main():

    browser = None

    try:

        print("=" * 60)
        print("TECHNOFUNDA AUTOMATION HUB")
        print("Version : 1.0.1")
        print("=" * 60)

        browser = BrowserService()

        run(browser.page)

        print("=" * 60)
        print("Automation Completed Successfully")
        print("=" * 60)

    except KeyboardInterrupt:

        print("\nAutomation cancelled by user.")

    except Exception:

        print("\n" + "=" * 60)
        print("FATAL ERROR")
        print("=" * 60)

        traceback.print_exc()

        print("=" * 60)

    finally:

        if browser is not None:
            browser.close()

        print("\nBrowser Closed.")


if __name__ == "__main__":
    main()