from Satellite import Satellite
from Station import Station
import Datefun as df
import Fileio as fi

constellation = []
constellation.append(Satellite("TLE.txt"))
print("----------------------")
print("Sattelite Test")
print("name " + str(constellation[0].name))
print("refepoch " + str(constellation[0].refepoch))
print("incl " + str(constellation[0].incl))
print("raan " + str(constellation[0].raan))
print("eccn " + str(constellation[0].eccn))
print("arg_per " + str(constellation[0].arg_per))
print("mean_an " + str(constellation[0].mean_an))
print("mean_mo " + str(constellation[0].mean_mo))
print("ndot2 " + str(constellation[0].ndot2))
print("nddot6 " + str(constellation[0].nddot6))
print("bstar " + str(constellation[0].bstar))
print("orbitnum " + str(constellation[0].orbitnum))

station = Station("station.dat")
print("----------------------")
print("Station Test")
print("name " + str(station.name))
#print("stnlat " + str(station.stnlat))
print("stnlon " + str(station.stnlon))
print("stnalt " + str(station.stnalt))
print("utc_offset " + str(station.utc_offset))
print("st_az_speed_max " + str(station.st_az_speed_max))
print("st_el_speed_max " + str(station.st_el_speed_max))
print("az_el_lim " + str(station.az_el_lim))
print("az_el_nlim " + str(station.az_el_nlim))

print("----------------------")
print("Datefun Test")
print("doy " + str(df.doy(2000, 12, 31)))
print("frcofd " + str(df.frcofd(12,0,0)))
print("ep2dat " + str(df.ep2dat("0" + str(constellation[0].refepoch))))
print("curday " + str(df.curday()))

print("----------------------")
print("Fileio Test")
fi.banner()
fi.errmsg("this is a test error")