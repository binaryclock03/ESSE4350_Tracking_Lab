from python_lib.Satellite import Satellite
import python_lib.Datefun as df

sat = Satellite("inputs/TLE.txt")

date = df.ep2dat(sat.refepoch)
print(date)
print(df.days_since_J2000(date.year, date.month, date.day))