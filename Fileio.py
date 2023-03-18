from Station import Station
from Satellite import Satellite

def banner():
    ver = 0.1
    welcome_msg = "Hello we are the two called Luke and Daniel"
    print(f"ESSE4350 2023-03-06 v{ver}\n{welcome_msg}")

def anykey():
    input("Press enter to continue...")

def errmsg(error_str):
    print("[ERROR] " + error_str)

def ReadStationFile(station_file_path) -> Station:
    return Station(station_file_path)

def ReadNoradTLE(sattelite_file_path) -> Satellite:
    return Satellite(sattelite_file_path)

def STKout(EphemFile, StartString, epsec, Coord, time, position, velocity):
    num_points = len(time)
    to_write = []
    to_write.append("stk.v.4.3")
    to_write.append("")
    to_write.append("BEGIN Ephemeris")
    to_write.append("")
    to_write.append("NumberOfEphemerisPoints " + str(num_points))
    to_write.append("")
    to_write.append("ScienarioEpoch " + StartString)
    to_write.append("InterpolationMethod Lagrange")
    to_write.append("InterpolationOrder 7")
    to_write.append("CentralBody Earth")
    to_write.append("CoordinateSystem " + Coord)
    to_write.append("")
    to_write.append("EphemerisTimePosVel")
    to_write.append("")
    
    for i in range(num_points):
        to_write.append(str(time[i] + epsec) + " " 
                        + str(position[i][0]) + " "
                        + str(position[i][1]) + " " 
                        + str(position[i][2]) + " "
                        + str(velocity[i][0]) + " "
                        + str(velocity[i][1]) + " "
                        + str(velocity[i][2]))

    to_write.append("")
    to_write.append("END Ephemeris")

    for i in range(len(to_write)):
        to_write[i] += "\n"

    with open("thing.e", 'w') as file:
        file.writelines(to_write)

def STKout_sp(SPFile, epsec, time, Azimuth, Elevation):
    num_points = len(time)
    to_write = []
    to_write.append("stk.v.4.3")
    to_write.append("Begin Attitude")
    to_write.append("NumberofAttitudePoints " + str(num_points))
    to_write.append("Sequence 313")
    to_write.append("AttitudeTimeAzElAngles")
    
    for i in range(num_points):
        to_write.append(str(time[i] + epsec) + " " 
                        + str(Azimuth[i]) + " "
                        + str(Elevation[i]))

    to_write.append("End Attitude")

    for i in range(len(to_write)):
        to_write[i] += "\n"

    with open(SPFile, 'w') as file:
        file.writelines(to_write)

STKout("thing.e", "hello", 20, "J2000", [0], [(1.847,2,3)], [(6,5,4)])
STKout_sp("sensor_pointing.sp", 10, [1,2], [0,1], [2,4])