from ctypes import *
#load the shared object file
getV = CDLL('./getVoltage.so')
 
#Find sum of integers
#print('go to load\n')
res_int32_t = getV.getVoltage()
res_int32_t.restype = POINTER(c_long)
print (res_int32_t)
