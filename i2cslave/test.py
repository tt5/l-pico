import utime
from machine import mem32
from i2cSlave import i2c_slave

s_i2c = i2c_slave(0,sda=6,scl=7,slaveAddress=0x41)
counter =1
try:
    while True:
        if s_i2c.any():
            #print(s_i2c.get())
            aa = s_i2c.get()
            print(aa)
            if aa == 12:
                led_onboard.value(1)
            if aa == 15:
                led_onboard.value(0)
        if s_i2c.anyRead():
            counter = counter + 1
            s_i2c.put(counter & 0xff)
            print(counter)
    
except KeyboardInterrupt:
    pass
