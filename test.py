from ctypes import *
 
#load the shared object file
getVoltage = CDLL('./getVoltage.so')
 
#Find sum of integers
res_int = getVoltage._get()
print (str(res_int))
