from ctypes import *
#load the shared object file
getV = CDLL('./getVoltage.so')
 
#Find sum of integers
res_int = getV.getVoltage()
print (res_int)
