from ctypes import *
import time
#load the shared object file

getV = CDLL('./getVoltage.so')

'''
ch_0 = c_int32(0)
ch_1 = c_int32(0)
ch_2 = c_int32(0)
ch_3 = c_int32(0)
ch_4 = c_int32(0)
ch_5 = c_int32(0)
ch_6 = c_int32(0)
ch_7 = c_int32(0)

class Voltage(Structure):
	_fields_ = [('ch_0',c_int32),
			 ('ch_1',c_int32),
			 ('ch_2',c_int32),
			 ('ch_3',c_int32),
			 ('ch_4',c_int32),
			 ('ch_5',c_int32),
			 ('ch_6',c_int32),
			 ('ch_7',c_int32)]
volt = Voltage()
volt.ch_0 = ch_0
volt.ch_1 = ch_1
volt.ch_2 = ch_2
volt.ch_3 = ch_3
volt.ch_4 = ch_4
volt.ch_5 = ch_5
volt.ch_6 = ch_6
volt.ch_7 = ch_7

#getV.getVoltage.restype = POINTER(c_int32)

start = time.time()
getV.getVoltage.restype = POINTER(Voltage)
res_int32_t = getV.getVoltage()
end = time.time()
print (end-start)

print (res_int32_t.contents.ch_0)
print (res_int32_t.contents.ch_1)
print (res_int32_t.contents.ch_2)
print (res_int32_t.contents.ch_3)
print (res_int32_t.contents.ch_4)
'''

volt_stru = c_int32 * 8
volt =volt_stru()
start = time.time()
getV.getVoltage.restype = POINTER(volt_stru)
volt = getV.getVoltage()
end = time.time()
print (end-start)

print (volt[2])
