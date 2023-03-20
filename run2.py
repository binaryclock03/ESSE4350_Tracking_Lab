from python_lib.satellite import Satellite
import python_lib.datefun as df

sat = Satellite("inputs/TLE.txt")

epoch = 23062.38276793

date = df.ep2dat(epoch)
print(df.seconds_to_midnight(epoch))
print(date)
print(df.days_since_J2000(date.year, date.month, date.day))