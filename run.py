from python_lib.Datefun import *
from python_lib.Fileio import *
from python_lib.Satellite import *
from python_lib.Station import *
from datetime import datetime
import os
import glob

## User defined stuff
tracking_year   = 2023
tracking_month, month_name = 4, "Apr"
tracking_day    = 2
tracking_hour   = 19
tracking_minute = 0

# tracking duration in seconds
tracking_duration = 60*60
tracking_resolution = 5

tracking_datetime = datetime(tracking_year, tracking_month, tracking_day, tracking_hour, tracking_minute, 0)
days = int(days_since_J2000(tracking_year, tracking_month, tracking_day))
hours = tracking_hour + (tracking_minute/60)

constellation_inputs = ReadNoradTLE("inputs\\gp.txt")
station = ReadStationFile("inputs\\station.dat")
constellation_outputs = {}

constellation_AOS_LOS = {}

# sanitize output folder
folders = glob.glob('outputs/*')
for folder in folders:
    for file in glob.glob(f'{folder}/*'):
      os.remove(file)
    os.rmdir(folder)

## runing the model
from OMPython import ModelicaSystem

model = ModelicaSystem(os.getcwd() + "\\OpenModelica\\Sattrak.mo","Sattrak.Sat_Test",["Modelica.Constants"])

for sat in constellation_inputs.values():
    if sat.name == "SBIII-5(PRN11)":
      offset = 0
      running = True
      local_resolution = tracking_resolution
      local_duration = tracking_duration
      local_hours = hours

      while(running):
        local_tstart_ref = (tracking_datetime-ep2dat(sat.refepoch)) 
        local_tstart = local_tstart_ref.days * (60*60*24) + local_tstart_ref.seconds + offset
        local_hours = hours + (offset/3600)

        print(f"\nSimulating {sat.name}")
        model.setParameters([f"tstart={local_tstart}", f"M0={sat.mean_an}", f"N0={sat.mean_mo}", f"i={sat.incl}", f"w0={sat.arg_per}",
                            f"eccn={sat.eccn}", f"RAAN0={sat.raan}", f"Ndot2={sat.ndot2}", f"Nddot6={sat.nddot6}",
                            f"stn_long={station.stnlon}", f"stn_lat={station.stnlat}", f"stn_elev={station.stnalt}",
                            f"days={days}", f"hours={local_hours}"])
        
        model.setSimulationOptions(["startTime=0.", f"stopTime={local_duration}", f"stepSize={local_resolution}"])
        model.simulate()
        output = model.getSolutions(["time",
                                    "p_sat_ECI[1]", "p_sat_ECI[2]", "p_sat_ECI[3]",
                                    "v_sat_ECI[1]", "v_sat_ECI[2]", "v_sat_ECI[3]",
                                    "p_sat_ECF[1]", "p_sat_ECF[2]", "p_sat_ECF[3]",
                                    "v_sat_ECF[1]", "v_sat_ECF[2]", "v_sat_ECF[3]",
                                    "p_sat_topo[1]", "p_sat_topo[2]", "p_sat_topo[3]",
                                    "v_sat_topo[1]", "v_sat_topo[2]", "v_sat_topo[3]",
                                    "Elevation", "Azimuth"])
        
        # gathering outputs for el az check
        time = output[0] + offset
        el, az = output[19], output[20]

        # doing az el check
        AOS_time = []
        AOS_bool = False
        LOS_time = []
        for i, elevation in enumerate(el):
          if elevation > 9 and elevation < 89:
            if not AOS_bool:
              print(f"found AOS {time[i]}")
              AOS_time.append(time[i])
              AOS_bool = True
          else:
            if AOS_bool:
              print(f"found LOS {time[i]}")
              LOS_time.append(time[i])
              AOS_bool = False

        constellation_AOS_LOS.update({sat.name:[AOS_time, LOS_time]})
        constellation_outputs.update({sat.name: output})

        if not local_duration == tracking_duration:
          running = False

        if running:
          if len(AOS_time) > 0:
            offset = AOS_time[0]-tracking_resolution
            local_duration = tracking_resolution*2
            local_resolution = tracking_resolution/1000
            print("resiming")
          else:
            running = False
          
      # gathering other outputs
      px_ECI, py_ECI, pz_ECI = output[1], output[2], output[3]
      vx_ECI, vy_ECI, vz_ECI = output[4], output[5], output[6]
      px_ECF, py_ECF, pz_ECF = output[7], output[8], output[9]
      vx_ECF, vy_ECF, vz_ECF = output[10], output[11], output[12]
      px_TOPO, py_TOPO, pz_TOPO = output[13], output[14], output[15]
      vx_TOPO, vy_TOPO, vz_TOPO = output[16], output[17], output[18]

      p_ECI = list(zip(px_ECI, py_ECI, pz_ECI))
      v_ECI = list(zip(vx_ECI, vy_ECI, vz_ECI))

      p_ECF = list(zip(px_ECF, py_ECF, pz_ECF))
      v_ECF = list(zip(vx_ECF, vy_ECF, vz_ECF))

      p_TOPO = list(zip(px_TOPO, py_TOPO, pz_TOPO))
      v_TOPO = list(zip(vx_TOPO, vy_TOPO, vz_TOPO))

      # create dir to put the output files into
      os.mkdir(f"outputs\\{sat.name}")
      STKout(f"outputs\\{sat.name}\\ECI_{sat.name}.e", f"{tracking_day} {month_name} {tracking_year} {int(tracking_hour)}:{tracking_minute}:00", 0, "Custom TEMED", time, p_ECI, v_ECI)
      STKout(f"outputs\\{sat.name}\\ECF_{sat.name}.e", f"{tracking_day} {month_name} {tracking_year} {int(tracking_hour)}:{tracking_minute}:00", 0, "Fixed", time, p_ECF, v_ECF)
      STKout(f"outputs\\{sat.name}\\TOPO_{sat.name}.e", f"{tracking_day} {month_name} {tracking_year} {int(tracking_hour)}:{tracking_minute}:00", 0, "Custom Facility/ARO Gnd_topo_sys", time, p_TOPO, v_TOPO)
      STKout_sp(f"outputs\\{sat.name}\\POINT_{sat.name}.sp", 0, time, az, el)

# get rid of files generated by OMPython
from pathlib import Path
dir = Path.cwd()
files = dir.glob("Sattrak.Sat_Test*")
for fi in files:
  fi.unlink()


print(constellation_AOS_LOS)

exit()

## Plotting stuff
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