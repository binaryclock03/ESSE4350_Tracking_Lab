from python_lib.satellite import Satellite
import python_lib.fileio as fi
import python_lib.datefun as df
from python_lib.fileio import ReadNoradTLE

const = ReadNoradTLE("inputs/TLE.txt")
sat = const.get(list(const.keys())[0])

epoch = sat.refepoch
print(sat.refepoch)

fi.linespace()
print(sat)


date = df.ep2dat(epoch)
print(df.seconds_to_midnight(epoch))
print(date)
print(df.days_since_J2000(date.year, date.month, date.day))