"""
AutomationHub Logger Service
"""

import time
import traceback

from datetime import datetime
from zoneinfo import ZoneInfo

from src.config.version import APP_NAME, VERSION, BUILD


class Logger:

    def __init__(self):

        self.timezone = ZoneInfo("Asia/Kolkata")

    # =====================================================
    # Date & Time
    # =====================================================

    def now(self):
        return datetime.now(self.timezone)

    def date(self):
        return self.now().strftime("%d-%b-%Y")

    def time(self):
        return self.now().strftime("%H:%M:%S")

    # =====================================================
    # Internal Logger
    # =====================================================

    def _log(self, level: str, message: str):

        print(
            f"[{self.date()} {self.time()}] "
            f"{level:<8} {message}",
            flush=True
        )

    # =====================================================
    # Standard Logging
    # =====================================================

    def info(self, message):
        self._log("INFO", message)

    def success(self, message):
        self._log("SUCCESS", message)

    def warning(self, message):
        self._log("WARNING", message)

    def error(self, message):
        self._log("ERROR", message)

    # =====================================================
    # Banner
    # =====================================================

    def banner(self, title=None):

        if title is None:
            title = APP_NAME

        print()
        print("=" * 60)
        print(title)
        print(f"Version : {VERSION}")
        print(f"Build   : {BUILD}")
        print("=" * 60)

    # =====================================================
    # Sections
    # =====================================================

    def section(self, title):

        print()
        print("-" * 70)
        print(title)
        print("-" * 70)

    def line(self):

        print("-" * 70)

    # =====================================================
    # Module Logging
    # =====================================================

    def start(self, module):

        self.info(f"{module} Started.")

    def finish(self, module):

        self.success(f"{module} Completed.")

    # =====================================================
    # Exception Logging
    # =====================================================

    def exception(self, ex: Exception):

        self.error(f"{type(ex).__name__}: {ex}")
        print(traceback.format_exc(), flush=True)

    # =====================================================
    # Performance Timer
    # =====================================================

    def timer(self):

        return time.perf_counter()

    def elapsed(self, start_time):

        return round(time.perf_counter() - start_time, 2)

    # =====================================================
    # Future Notification Hooks
    # =====================================================

    def google_sheet(self, *args, **kwargs):
        pass

    def telegram(self, *args, **kwargs):
        pass

    def email(self, *args, **kwargs):
        pass

    def slack(self, *args, **kwargs):
        pass


logger = Logger()