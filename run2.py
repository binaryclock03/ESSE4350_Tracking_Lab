from Satellite import Satellite
from Station import Station
import Datefun as df
import Fileio as fi

sat = Satellite("TLE.txt")

date = df.ep2dat(sat.refepoch)
print(date)
print(df.days_since_J2000(date.year, date.month, date.day))