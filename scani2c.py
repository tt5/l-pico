from machine import Pin, SoftI2C

i2c = SoftI2C(scl=Pin(7), sda=Pin(6))

devices = i2c.scan()

if len(devices) == 0:
  print("No i2c device !")
else:
  print('i2c devices found:', len(devices))

  for device in devices:
    print("I2C hexadecimal address: ", hex(device))

