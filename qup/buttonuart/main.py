from machine import Pin, UART
from time import sleep

b1 = Pin(16, Pin.IN, Pin.PULL_UP)
uart = UART(0, tx=Pin(0), rx=Pin(1))
uart.init()

uart.write("start")
while True:
    if b1.value() == 0 :
        uart.write("x")
    sleep(0.2)

