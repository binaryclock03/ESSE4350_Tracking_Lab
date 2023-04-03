from python_lib.Datefun import *
from python_lib.Fileio import *
from python_lib.Satellite import *
from python_lib.Station import *
from datetime import datetime

## User defined stuff
tracking_year   = 2023
tracking_month, month_name = 4, "Apr"
tracking_day    = 2
tracking_hour   = 19
tracking_minute = 0

# tracking duration in seconds
tracking_duration = 60*60*24

tracking_datetime = datetime(tracking_year, tracking_month, tracking_day, tracking_hour, tracking_minute, 0)
days = int(days_since_J2000(tracking_year, tracking_month, tracking_day))
hours = tracking_hour + (tracking_minute/60)

constellation_inputs = ReadNoradTLE("inputs\\gp.txt")
station = ReadStationFile("inputs\\station.dat")
constellation_outputs = {}

## runing the model
from OMPython import ModelicaSystem

model = ModelicaSystem("C:/Users/binar/Documents/Workshop/School/ENG4350/ESSE4350_Tracking_Lab/OpenModelica/Sattrak.mo","Sattrak.Sat_Test",["Modelica.Constants"])

for sat in constellation_inputs.values():
    tstart = (tracking_datetime-ep2dat(sat.raefepoch))
    tstart = tstart.days * (60*60*24) + tstart.seconds
    print(f"\nSimulating {sat.name}")
    model.setParameters([f"tstart={tstart}", f"M0={sat.mean_an}", f"N0={sat.mean_mo}", f"i={sat.incl}", f"w0={sat.arg_per}",
                         f"eccn={sat.eccn}", f"RAAN0={sat.raan}", f"Ndot2={sat.ndot2}", f"Nddot6={sat.nddot6}",
                         f"stn_long={station.stnlon}", f"stn_lat={station.stnlat}", f"stn_elev={station.stnalt}",
                         f"days={days}", f"hours={hours}"])

    model.setSimulationOptions(["startTime=0.", f"stopTime={tracking_duration}", "stepSize=200"])
    model.simulate()
    output = model.getSolutions(["time",
                                 "p_sat_topo[1]", "p_sat_topo[2]", "p_sat_topo[3]",
                                 "v_sat_topo[1]", "v_sat_topo[2]", "v_sat_topo[3]",
                                 "Elevation", "Azimuth"])
    constellation_outputs.update({sat.name: output})

    time = output[0]
    px, py, pz = output[1], output[2], output[3]
    vx, vy, vz = output[4], output[5], output[6]
    el, az = output[7], output[8]

    p = list(zip(px, py, pz))
    v = list(zip(vx, vy, vz))

    STKout(f"outputs\\ephem_{sat.name}.e", f"{tracking_day} {month_name} {tracking_year} {int(tracking_hour)}:{tracking_minute}:00", 0, "Fixed", time, p, v)
    STKout_sp(f"outputs\\pointing_{sat.name}.sp", 0, time, az, el)

# get rid of files generated by OMPython
from pathlib import Path
dir = Path.cwd()
files = dir.glob("Sattrak.Sat_Test*")
for fi in files:
  fi.unlink()

key = list(constellation_outputs.keys())[14]
print(key)
time = constellation_outputs.get(key)[0]
p_sat_ECF_x = constellation_outputs.get(key)[1]
p_sat_ECF_y = constellation_outputs.get(key)[2]
p_sat_ECF_z = constellation_outputs.get(key)[3]
v_sat_ECF_x = constellation_outputs.get(key)[4]
v_sat_ECF_y = constellation_outputs.get(key)[5]
v_sat_ECF_z = constellation_outputs.get(key)[6]

az = constellation_outputs.get(key)[7]
el = constellation_outputs.get(key)[8]

from matplotlib import pyplot as plt
plt.figure(1)
plt.plot(time, p_sat_ECF_x)
plt.plot(time, p_sat_ECF_y)
plt.plot(time, p_sat_ECF_z)
plt.figure(2)
plt.plot(time, az)
plt.plot(time, el)
plt.show()