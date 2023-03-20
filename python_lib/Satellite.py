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

    def __init__(self, lines):
        self.name = str(lines[0][2:]).replace("\n", "")
        self.refepoch = float(lines[1][17:32])
        self.incl = float(lines[2][8:16])
        self.raan = float(lines[2][17:25])
        self.eccn = float("."+lines[2][26:33])
        self.arg_per = float(lines[2][34:42])
        self.mean_an = float(lines[2][43:51])
        self.mean_mo = float(lines[2][52:63])
        self.orbitnum = int(lines[2][63:68])
        self.ndot2 = float(lines[1][33:43])
        self.nddot6 = float("."+lines[1][45:50]) * (10** float(lines[1][51:52]))
        self.bstar = float("."+lines[1][54:59]) * (10** float(lines[1][60:61]))

    def __str__(self):
        string = ""
        string += ('Name: "' + self.name + '"\n')
        string += ("Ref Epoch: " + str(self.refepoch) + "\n")
        string += ("Inclination: " +str(self.incl) + "\n")
        string += ("Raan: " + str(self.raan) + "\n")
        string += ("Eccn: " + str(self.eccn) + "\n")
        string += ("Arg Per: " + str(self.arg_per )+ "\n")
        string += ("Mean Anomoly: " + str(self.mean_an) + "\n")
        string += ("Mean Motion: " + str(self.mean_an )+ "\n")
        string += ("Orbitnum: " + str(self.orbitnum) + "\n")
        string += ("Ndot2: " + str(self.ndot2) + "\n")
        string += ("Nddot6: " + str(self.nddot6) + "\n")
        string += ("Bstar: " + str(self.bstar) + "\n")
        return string

        