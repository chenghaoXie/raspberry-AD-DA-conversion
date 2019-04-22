from ctypes import *
#load the shared object file
getV = CDLL('./getVoltage.so')
 
#Find sum of integers
#print('go to load\n')
getV.getVoltage.restype = POINTER(c_int32)
res_int32_t = getV.getVoltage()
print (res_int32_t(2))
