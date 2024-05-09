from machine import Pin, UART

uart = UART(0, tx=Pin(0), rx=Pin(1))
uart.init()
uart.write("some")
uart.any()
uart.read()
