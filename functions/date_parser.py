import re
from datetime import datetime, timedelta
import logging
from zoneinfo import ZoneInfo

def parse_datetime(date_time_str: str) -> datetime.date:
    """Parse the date and time string into a datetime object."""
    # Example date_time_str: "Sep 18, 2024 at 7:00 am ET"
    try:
        # Remove the time zone abbreviation
        date_time_str = re.sub(r' ET$', '', date_time_str)
        datetime_value =  datetime.strptime(date_time_str,"%b %d, %Y at %I:%M %p")
        return datetime_value.date()
    except ValueError as e:
        logging.error(f"Date parsing error: {e}")
        return None

def convert_timezone(target_date: datetime.date, timezone: str) -> datetime.date:
    utc_datetime = datetime.combine(target_date, datetime.min.time(), tzinfo=ZoneInfo('UTC'))
    converted_datetime = utc_datetime.astimezone(ZoneInfo(timezone))
    return converted_datetime.date()



def date_test():
    today = datetime.now().date()
    yesterday = today - timedelta(days=1)
    print(yesterday)

    date_time_str = re.sub(r' ET$', '', "Sep 18, 2024 at 7:00 am ET")
    print(datetime.strptime(date_time_str,"%b %d, %Y at %I:%M %p").date())


if __name__ == "__main__":
    date_test()