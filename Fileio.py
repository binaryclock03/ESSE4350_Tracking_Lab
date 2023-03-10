from Station import Station
from Satellite import Satellite

def banner():
    ver = 0.1
    welcome_msg = "Hello we are the two called Luke and Daniel"
    print(f"ESSE4350 2023-03-06 v{ver}\n{welcome_msg}")

def anykey():
    pass

def errmsg(error_str):
    print("[ERROR] " + error_str)

def ReadStationFile(station_file_path) -> Station:
    return Station(station_file_path)

def ReadNoradTLE(sattelite_file_path) -> Satellite:
    return Satellite(sattelite_file_path)