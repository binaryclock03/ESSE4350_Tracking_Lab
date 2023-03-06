import datetime as dt

def doy(year, month, day):
    d0 = dt.date(year, 1, 1)
    d1 = dt.date(year, month, day)
    return (d1 - d0).days

def frcofd():
    pass

def ep2dat():
    pass

def curday():
    pass