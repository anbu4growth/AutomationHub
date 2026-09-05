from datetime import datetime
import pytz

IST = pytz.timezone("Asia/Kolkata")


def now():
    return datetime.now(IST)


def current_date():
    return now().strftime("%d-%b-%Y")


def current_time():
    return now().strftime("%H:%M:%S")


def timestamp():
    return now().strftime("%Y%m%d-%H%M%S")