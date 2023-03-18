class Satellite():
    name:str
    refepoch:float
    incl:float
    raan:float
    eccn:float
    arg_per:float
    mean_an:float
    mean_mo:float
    ndot2:float
    nddot6:float
    bstar:float
    orbitnum:int

    def __init__(self, sattelite_file_path):
        with open(sattelite_file_path) as file:
            lines = file.readlines()

            self.name = str(lines[0][2:]).replace("\n", "")
            self.refepoch = float(lines[1][16:30])
            self.incl = float(lines[2][7:16])
            self.raan = float(lines[2][16:25])
            self.eccn = float("0." + lines[2][25:33])
            self.arg_per = float(lines[2][33:42])
            self.mean_an = float(lines[2][42:51])
            self.mean_mo = float(lines[2][51:61])
            self.orbitnum = int(lines[2][61:66])
            self.ndot2 = float(lines[1][30:40])
            self.nddot6 = float(lines[1][42:46])
            self.bstar = float(lines[1][49:54])