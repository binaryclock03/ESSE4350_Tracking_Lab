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
    
    return dt.datetime(year, 1, 1, hours, minutes, seconds) + dt.timedelta(days=(days-1))

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

def month_num_to_name(month_numb):
    if month_numb == 1:    return "Jan"
    elif month_numb == 2:  return "Feb"
    elif month_numb == 3:  return "Mar"
    elif month_numb == 4:  return "Apr"
    elif month_numb == 5:  return "May"
    elif month_numb == 6:  return "Jun"
    elif month_numb == 7:  return "Jul"
    elif month_numb == 8:  return "Aug"
    elif month_numb == 9:  return "Sep"
    elif month_numb == 10: return "Oct"
    elif month_numb == 11: return "Nov"
    elif month_numb == 12: return "Dec"

def deg_splitter(degrees):
    if degrees < 0:
        degrees += 360
    deg = int(degrees)
    arc_min = int((degrees-deg) * 60)
    arc_sec = ((degrees-deg)*60 -arc_min) * 60
    return deg, arc_min, arc_sec