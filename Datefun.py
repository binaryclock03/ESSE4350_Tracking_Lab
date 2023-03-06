import datetime as dt

def doy(year:int, month:int, day:int) -> float:
    """Takes in the current year, month, and day and returns the number of days since the begining of the year"""
    d0 = dt.date(year, 1, 1)
    d1 = dt.date(year, month, day)
    return float((d1 - d0).days)

def frcofd(hour:int, minute:int, second:int) -> float:
    """Takes in the current hour, minute, and second and returns the fraction of the day"""
    sec = hour * 360 + minute * 60 + second
    return float(sec/(24*60*60))

def ep2dat(julian_date) -> dt.datetime:
    """Takes in the julian date and returns the current datetime in <YYYY-MM-DD HH:MM:SS> format"""
    greg_date = dt.datetime(1, 1, 1, 0, 0, 0) + dt.timedelta(days=julian_date)
    return greg_date

def curday() -> dt.datetime:
    """Returns the current datetime in <YYYY-MM-DD HH:MM:SS> format"""
    now = dt.datetime.now()
    return now.utcnow()