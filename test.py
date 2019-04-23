from ctypes import *
import time
#load the shared object file

getV = CDLL('./getVoltage.so')

cha = 8
#volt =(c_int32 * cha)()
start = time.time()
getV.getVoltage.restype = POINTER(c_int32 * cha)
volt = getV.getVoltage()
end = time.time()
print (end-start)

for i in range(0, cha):
     print(volt.contents[i])
