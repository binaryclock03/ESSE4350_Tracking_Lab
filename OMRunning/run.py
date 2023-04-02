from OMPython import ModelicaSystem

model = ModelicaSystem("C:/Users/binar/Documents/Workshop/School/ENG4350/ESSE4350_Tracking_Lab/OpenModelica/Sattrak.mo","Sattrak.GMST",["Modelica.Constants"])

tracking_year   = 2023
tracking_month  = 3
tracking_day    = 31
tracking_hour   = 14
tracking_minute = 0

from python_lib.Datefun import days_since_J2000
days = days_since_J2000(tracking_year, tracking_month, tracking_day)
tracking_hour += tracking_minute * (1/60)

model.setParameters(["days="+str(days), "hours="+str(tracking_hour)])
print(model.getParameters())
model.setSimulationOptions(["startTime=0.", "stopTime=1", "stepSize=1"])

model.simulate()
output = print(model.getSolutions(["time", "GMST"]))

print(output)