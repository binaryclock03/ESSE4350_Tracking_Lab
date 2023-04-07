from python_lib.Datefun import *
from python_lib.Fileio import *
from python_lib.Satellite import *
from python_lib.Station import *
from datetime import datetime, timedelta
import os
import glob
import numpy as np

constellation_inputs = read_TLE_file("inputs\\gp.txt")
station = read_stn_file("inputs\\station.dat")
tracking_datetime, tracking_duration, tracking_resolution = read_schedule_file("inputs\\tracking_schedule.txt")

month_name = month_num_to_name(tracking_datetime.month)
days = int(days_since_J2000(tracking_datetime.year, tracking_datetime.month, tracking_datetime.day))
hours = tracking_datetime.hour + (tracking_datetime.minute/60) + (tracking_datetime.second/3600)

constellation_outputs = {}
constellation_AOS_LOS = {}
constellation_LINK = {}

# sanitize output folder
folders = glob.glob('outputs/*')
for folder in folders:
    for file in glob.glob(f'{folder}/*'):
      os.remove(file)
    os.rmdir(folder)

## runing the model
from OMPython import ModelicaSystem

model = ModelicaSystem("Sattrak.mo","Sattrak.Sat_Test",["Modelica.Constants"])

for sat in constellation_inputs.values():
  if True:#sat.name == "SBIIR-9(PRN21)":
    tstart_ref = (tracking_datetime-ep2dat(sat.refepoch)) 
    tstart = tstart_ref.days * (60*60*24) + tstart_ref.seconds

    ## Simulating stuff first pass
    print(f"\nSimulating {sat.name}")

    model.setParameters([f"tstart={tstart}", f"M0={sat.mean_an}", f"N0={sat.mean_mo}", f"i={sat.incl}", f"w0={sat.arg_per}",
                          f"eccn={sat.eccn}", f"RAAN0={sat.raan}", f"Ndot2={sat.ndot2}", f"Nddot6={sat.nddot6}",
                          f"stn_long={station.stnlon}", f"stn_lat={station.stnlat}", f"stn_elev={station.stnalt}",
                          f"days={days}", f"hours={hours}"])
    
    model.setSimulationOptions(["startTime=0.", f"stopTime={(tracking_duration.seconds)+(tracking_duration.days*60*60*24)}", f"stepSize={tracking_resolution}"])
    model.simulate()

    print("getting solutions")
    # output = model.getSolutions(["time",
    #                             "p_sat_ECI[1]", "p_sat_ECI[2]", "p_sat_ECI[3]",
    #                             "v_sat_ECI[1]", "v_sat_ECI[2]", "v_sat_ECI[3]",
    #                             "p_sat_ECF[1]", "p_sat_ECF[2]", "p_sat_ECF[3]",
    #                             "v_sat_ECF[1]", "v_sat_ECF[2]", "v_sat_ECF[3]",
    #                             "p_sat_topo[1]", "p_sat_topo[2]", "p_sat_topo[3]",
    #                             "v_sat_topo[1]", "v_sat_topo[2]", "v_sat_topo[3]",
    #                             "Elevation", "Azimuth"])

    output = model.getSolutions(["time", "Elevation", "Azimuth", "Range", "Elrate", "Azrate"])
    
    constellation_outputs.update({sat.name: output})

    # gathering outputs for el az check
    time = output[0] 
    el, az, range = output[1], output[2], output[3]

    # doing az el check
    AOS_time = []
    AOS_bool = False
    LOS_time = []

    print("looking for AOL LOS")
    for i, elevation in enumerate(el):
      if elevation >= station.az_el_lim[0][1] and elevation <= station.az_el_lim[0][2]:
        if not AOS_bool:
          print(f"found AOS {time[i]}")
          AOS_time.append(time[i])
          AOS_bool = True
      else:
        if AOS_bool:
          print(f"found LOS {time[i]}")
          LOS_time.append(time[i])
          AOS_bool = False
    
    # finding link
    frequency = 1.57e9
    EIRP_sat = 11.4 + 13
    PT_stn = 56 #- 10*np.log10(200)
    FSPL = 10*np.log10(((4*np.pi*np.array(range*1e3)*frequency)/3e8)**2)
    Link = PT_stn + EIRP_sat - FSPL

    constellation_AOS_LOS.update({sat.name:[AOS_time, LOS_time]})
    constellation_LINK.update({sat.name:Link})

    # gathering other outputs
    # px_ECI, py_ECI, pz_ECI = output[1], output[2], output[3]
    # vx_ECI, vy_ECI, vz_ECI = output[4], output[5], output[6]
    # px_ECF, py_ECF, pz_ECF = output[7], output[8], output[9]
    # vx_ECF, vy_ECF, vz_ECF = output[10], output[11], output[12]
    # px_TOPO, py_TOPO, pz_TOPO = output[13], output[14], output[15]
    # vx_TOPO, vy_TOPO, vz_TOPO = output[16], output[17], output[18]

    # p_ECI = list(zip(px_ECI, py_ECI, pz_ECI))
    # v_ECI = list(zip(vx_ECI, vy_ECI, vz_ECI))

    # p_ECF = list(zip(px_ECF, py_ECF, pz_ECF))
    # v_ECF = list(zip(vx_ECF, vy_ECF, vz_ECF))

    # p_TOPO = list(zip(px_TOPO, py_TOPO, pz_TOPO))
    # v_TOPO = list(zip(vx_TOPO, vy_TOPO, vz_TOPO))

    # create dir to put the output files into
    #os.mkdir(f"outputs\\{sat.name}")
    # STKout(f"outputs\\{sat.name}\\ECI_{sat.name}.e", f"{tracking_day} {month_name} {tracking_year} {int(tracking_hour)}:{tracking_minute}:00", 0, "Custom TEMED", time, p_ECI, v_ECI)
    # STKout(f"outputs\\{sat.name}\\ECF_{sat.name}.e", f"{tracking_day} {month_name} {tracking_year} {int(tracking_hour)}:{tracking_minute}:00", 0, "Fixed", time, p_ECF, v_ECF)
    # STKout(f"outputs\\{sat.name}\\TOPO_{sat.name}.e", f"{tracking_day} {month_name} {tracking_year} {int(tracking_hour)}:{tracking_minute}:00", 0, "Custom Gnd_topo_sys Facility/ARO", time, p_TOPO, v_TOPO)
    #STKout_sp(f"outputs\\{sat.name}\\POINT_{sat.name}.sp", 0, time, az, el)


# get rid of files generated by OMPython
from pathlib import Path
dir = Path.cwd()
files = dir.glob("Sattrak.Sat_Test*")
for fi in files:
  fi.unlink()


to_print = "\nSat#__Sat Name____________Access#___AOS Date Time___________LOS Date Time___________Duration__Min Power (dBm)"
for i, sat in enumerate(constellation_AOS_LOS.items()):
  if len(sat[1][0]) == 0:
    pass
  else:
    outputs = constellation_outputs.get(sat[0])
    to_print += f"\n{i}".ljust(7) + f"{sat[0]}".ljust(20)
    for i, aos in enumerate(sat[1][0]):
      aos_datetime = tracking_datetime + timedelta(seconds=aos)
      if i > 1:
        to_print += "\n".ljust(28)
      to_print += f"{i+1}".ljust(10) + f"{str(aos_datetime).split('.')[0]}".ljust(24)
      if len(sat[1][1]) > i:
        los = sat[1][1][i]
        los_datetime = tracking_datetime + timedelta(seconds=sat[1][1][i])
        to_print += f"{str(los_datetime).split('.')[0]}".ljust(24)
        to_print += f"{(los_datetime-aos_datetime).seconds + (los_datetime-aos_datetime).days*(60*60*24)}".ljust(10)
        
        aos_index = int(np.min(np.where(outputs[0] == aos)[0]))
        los_index = int(np.min(np.where(outputs[0] == los)[0]))

        link = constellation_LINK.get(sat[0])
        to_print += str(round(np.min(link[aos_index:los_index])+30,1))
                        
        # File creation
        os.mkdir(f"outputs\\{sat[0]}")
        STKout_sp(f"outputs\\{sat[0]}\\{sat[0]}_ACCESS{i+1}.sp", 0, outputs[0][aos_index:los_index], outputs[1][aos_index:los_index], outputs[2][aos_index:los_index])
        station_out(f"outputs\\{sat[0]}\\{sat[0]}_ACCESS_{i+1}.txt", tracking_datetime, outputs[0][aos_index:los_index], outputs[1][aos_index:los_index], outputs[1][aos_index:los_index], outputs[2][aos_index:los_index], outputs[2][aos_index:los_index])
      else: 
        end_time = tracking_datetime + tracking_duration
        to_print += f"{str(end_time).split('.')[0]}".ljust(24)
        to_print += f"{(end_time-aos_datetime).seconds + (end_time-aos_datetime).days*(60*60*24)}".ljust(10)

        aos_index = int(np.min(np.where(outputs[0] == aos)[0]))

        link = constellation_LINK.get(sat[0])
        to_print += str(round(np.min(link[aos_index:])+30,1))
    
        # File creation 
        os.mkdir(f"outputs\\{sat[0]}")
        STKout_sp(f"outputs\\{sat[0]}\\{sat[0]}_ACCESS_{i+1}.sp", 0, outputs[0][aos_index:], outputs[1][aos_index:], outputs[2][aos_index:])
        station_out(f"outputs\\{sat[0]}\\{sat[0]}_ACCESS_{i+1}.txt", tracking_datetime, outputs[0][aos_index:], 
                    outputs[1][aos_index:], outputs[4][aos_index:], 
                    outputs[2][aos_index:], outputs[5][aos_index:])

print(to_print)

exit()