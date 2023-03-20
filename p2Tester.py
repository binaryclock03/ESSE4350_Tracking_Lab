from python_lib.Fileio import *

STKout("outputs/thing.e", "hello", 20, "J2000", [0], [(100000 ,0,0)], [(0,0,0)])
print("hello")
anykey()
print("hello2")
STKout_sp("outputs/sensor_pointing.sp", 10, [1,2], [0,1], [2,4])