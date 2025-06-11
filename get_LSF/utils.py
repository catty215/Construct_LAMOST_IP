from datetime import datetime, timedelta

def convert_minutes_to_datetime(minutes_since_base):
    """
    Convert minutes since 1858-11-17 00:00:00 (MJD origin) to a datetime object.
    """
    base_time = datetime(1858, 11, 17, 0, 0, 0)
    specific_date = base_time + timedelta(minutes=minutes_since_base)
    return specific_date

def wl_range():
    """
    Return a wavelength range for each line profile.
    """
    return {
        4046.565: (4036, 4056), 4358.335: (4350, 4370),
        4678.149: (4668, 4688), 4799.912: (4790, 4810),
        5085.822: (5076, 5096), 5460.750: (5450, 5470),
        5790.67: (5781, 5801), 5944.834: (5935, 5958),
        6096.163: (6087, 6110), 6143.063: (6133, 6155),
        6266.495: (6256, 6278), 6334.428: (6325, 6347),
        6402.248: (6392, 6415), 6506.528: (6495, 6518),
        6598.953: (6588, 6611), 6678.276: (6667, 6690),
        6929.467: (6918, 6941), 7173.938: (7164, 7185),
        7245.167: (7235, 7255), 7438.898: (7428, 7450),
        7635.106: (7625, 7645), 8377.6065: (8368, 8390),
        8495.3598: (8485, 8508)
    }