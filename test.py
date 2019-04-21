from ctypes import *
#load the shared object file
getV = CDLL('./getVoltage.so')
 
#Find sum of integers
print('go to load\n')
res_int = getV.getVoltage()
print (res_int)
