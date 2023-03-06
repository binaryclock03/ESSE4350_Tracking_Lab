import datetime as dt

def doy(year, month, day):
    d0 = dt.date(year, 1, 1)
    d1 = dt.date(year, month, day)
    return (d1 - d0).days

def frcofd(hour, minute, second):
    sec = hour * 360 + minute * 60 + second
    return sec/(24*60*60)

def ep2dat():
    pass

def curday():
    pass