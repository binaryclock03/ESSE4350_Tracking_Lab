import datetime as dt
import math

def doy(year:int, month:int, day:int) -> float:
    """Takes in the current year, month, and day and returns the number of days since the begining of the year"""
    d0 = dt.date(year, 1, 1)
    d1 = dt.date(year, month, day)
    return float((d1 - d0).days)

def frcofd(hour:int, minute:int, second:int) -> float:
    """Takes in the current hour, minute, and second and returns the fraction of the day"""
    sec = (hour * 60 * 60) + (minute * 60) + second
    return float(sec/(24*60*60))

def ep2dat(epoch) -> dt.datetime:
    """Takes in the epoch and returns the current datetime in <YYYY-MM-DD HH:MM:SS> format"""
    epoch = str(epoch)
    year = int("20" + epoch[0:2])
    days = int(epoch[2:5])
    frcofd = float(epoch[5:])
    hours = math.floor(float(frcofd) * 24)
    minutes = math.floor((float(frcofd)*24 - hours) * 60)
    seconds = math.floor((((float(frcofd)*24 - hours) * 60) - minutes) * 60)
    
    return dt.datetime(year, 1, 1, hours, minutes, seconds) + dt.timedelta(days=days)

def curday() -> dt.datetime:
    """Returns the current datetime in <YYYY-MM-DD HH:MM:SS> format"""
    now = dt.datetime.now()
    return now.utcnow()

def days_since_J2000(year, month, day):
    """Returns the number of days from J200 to the given year month and day"""
    d0 = dt.date(2000, 1, 1)
    d1 = dt.date(year, month, day)
    return float((d1 - d0).days)

def seconds_to_midnight(epoch):
    """Returns the number of seconds from the Epoch to the next midnight"""
    d0 = ep2dat(epoch)
    d1 = dt.datetime(year=d0.year, month=d0.month, day=d0.day+1, hour=0)
    return float((d1 - d0).seconds)