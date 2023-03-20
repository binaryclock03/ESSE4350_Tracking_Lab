class Station():
    name:str
    stnlat:float
    stnlon:float
    stnalt:float
    utc_offset:float
    az_el_nlim:int
    az_el_lim:tuple
    st_az_speed_max:float
    st_el_speed_max:float

    def __init__(self, station_file_path):
        with open(station_file_path) as file:
            lines = file.readlines()
            
            for i, line in enumerate(lines):
                lines[i] = line.split("!", 1)[0].replace("\n", "")
            
            self.name = str(lines[0])
            self.stnlat = float(lines[1])
            self.stnlon = float(lines[2])
            self.stnalt = float(lines[3])
            self.utc_offset = float(lines[4])
            self.az_el_nlim = int(lines[5])

            az_el_lim = []
            for i in range(self.az_el_nlim):
                lim_tuple = lines[6+i].replace(" ", "").split(",")
                for i in range(len(lim_tuple)):
                    lim_tuple[i] = float(lim_tuple[i])
                az_el_lim.append(lim_tuple)
            self.az_el_lim = az_el_lim

            self.st_az_speed_max = float(lines[self.az_el_nlim - 1 + 7])
            self.st_el_speed_max = float(lines[self.az_el_nlim - 1 + 8])