from machine import Pin, ADC

b1_pin = Pin(26, mode=Pin.IN)
b1 = ADC(b1_pin)
print(b1.read_u16())

