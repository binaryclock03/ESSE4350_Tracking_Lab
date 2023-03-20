from python_lib.satellite import Satellite
from python_lib.station import Station
import python_lib.datefun as df
import python_lib.fileio as fi

constellation = fi.ReadNoradTLE("inputs/TLE.txt")
sat = constellation.get(list(constellation.keys())[0])

fi.linespace()
print("Sattelite Test")
print(sat)

station = Station("inputs/station.dat")
fi.linespace()
print("Station Test")
print("name " + str(station.name))
print("stnlat " + str(station.stnlat))
print("stnlon " + str(station.stnlon))
print("stnalt " + str(station.stnalt))
print("utc_offset " + str(station.utc_offset))
print("st_az_speed_max " + str(station.st_az_speed_max))
print("st_el_speed_max " + str(station.st_el_speed_max))
print("az_el_lim " + str(station.az_el_lim))
print("az_el_nlim " + str(station.az_el_nlim))

fi.linespace()
print("Datefun Test")
print("doy " + str(df.doy(2000, 12, 31)))
print("frcofd " + str(df.frcofd(12,0,0)))
print("ep2dat " + str(df.ep2dat(str(sat.refepoch))))
print("curday " + str(df.curday()))

fi.linespace()
print("Fileio Test")
fi.banner()
fi.errmsg("this is a test error")