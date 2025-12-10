from datetime import datetime, timedelta

def convert_minutes_to_datetime(minutes_since_base):
    """
    Convert minutes since 1858-11-17 00:00:00 (MJD origin) to a datetime object.
    """
    base_time = datetime(1858, 11, 17, 0, 0, 0)
    specific_date = base_time + timedelta(minutes=minutes_since_base)
    return specific_date