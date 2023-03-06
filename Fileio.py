from Station import *

def banner():
    ver = 0.1
    welcome_msg = "Hello we are the two idots called Luke and Daniel"
    print(f"ESSE4350 2023-03-06 v{ver}\n{welcome_msg}")

def anykey():
    pass

def errmsg(error_str):
    print("[ERROR] " + error_str)

def ReadStationFile(station_file_path) -> Station:
    return Station(station_file_path)

def ReadNoradTLE():
    pass