from python_lib.station import Station
from python_lib.satellite import Satellite

def banner():
    """Creates our standard banner and prints it to the console"""
    ver = 0.1
    welcome_msg = "Hello we are the two called Luke and Daniel"
    print(f"ESSE4350 2023-03-06 v{ver}\n{welcome_msg}")

def linespace():
    """Prints a linespace to the console"""
    print('------------------------')

def anykey():
    """Pauses program execution until any key on the keyboard is pressed"""
    import msvcrt as m
    m.getch()

def errmsg(error_str):
    """Prints an error msg to the console as <[ERROR] error_str>"""
    print("[ERROR] " + error_str)

def ReadStationFile(station_file_path) -> Station:
    """Reads a station file and returns it as a station object"""
    return Station(station_file_path)

def ReadNoradTLE(sattelite_file_path) -> dict:
    """Reads a TLE file and returns a dictionary of sattelites of form {name:str : Satellite}"""
    with open(sattelite_file_path) as file:
        lines = file.readlines()
        num_sats = len(lines)/3
        if num_sats != int(num_sats):
            errmsg("Non integer number of sattelites detected")
        num_sats = int(num_sats)

        constellation = {}
        for i in range(num_sats):
            sat = Satellite(lines[i:i+3])
            constellation.update({sat.name:sat})
    return constellation

def STKout(EphemFile, StartString, epsec, Coord, time, position, velocity):
    """Writes an ephem file with the parameters given"""
    # define how many point are in the file
    num_points = len(time)
    # define the to_write list
    to_write = []
    # append all the header stuff
    to_write.append("stk.v.4.3")
    to_write.append("")
    to_write.append("BEGIN Ephemeris")
    to_write.append("")
    to_write.append("NumberOfEphemerisPoints " + str(num_points))
    to_write.append("")
    to_write.append("ScenarioEpoch " + StartString)
    to_write.append("InterpolationMethod Lagrange")
    to_write.append("InterpolationOrder 7")
    to_write.append("CentralBody Earth")
    to_write.append("CoordinateSystem " + Coord)
    to_write.append("")
    to_write.append("EphemerisTimePosVel")
    to_write.append("")
    
    # loop through the points and add each vel and pos to the line
    for i in range(num_points):
        to_write.append(str(time[i] + epsec) + " " 
                        + str(position[i][0]) + " "
                        + str(position[i][1]) + " " 
                        + str(position[i][2]) + " "
                        + str(velocity[i][0]) + " "
                        + str(velocity[i][1]) + " "
                        + str(velocity[i][2]))

    # write end of file statement
    to_write.append("")
    to_write.append("END Ephemeris")

    # loop through all the lines and add pagebreaks
    for i in range(len(to_write)):
        to_write[i] += "\n"

    # actually write to_write into the file
    with open("thing.e", 'w') as file:
        file.writelines(to_write)

def STKout_sp(SPFile, epsec, time, Azimuth, Elevation):
    # define how many sensorpointing points will be in the file
    num_points = len(time)
    # generate a list of stuff to write, where each element is a single line
    to_write = []
    # add all the header stuff
    to_write.append("stk.v.4.3")
    to_write.append("Begin Attitude")
    to_write.append("NumberofAttitudePoints " + str(num_points))
    to_write.append("Sequence 313")
    to_write.append("AttitudeTimeAzElAngles")
    
    # here we loop through all the points, writing them into the to_write list
    for i in range(num_points):
        to_write.append(str(time[i] + epsec) + " " 
                        + str(Azimuth[i]) + " "
                        + str(Elevation[i]))

    # end out the file by adding the end command
    to_write.append("End Attitude")

    # now loop through all the lines and add pagebreaks
    for i in range(len(to_write)):
        to_write[i] += "\n"

    # write the to_write list to a file
    with open(SPFile, 'w') as file:
        file.writelines(to_write)

