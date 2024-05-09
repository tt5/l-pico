from machine import Pin, UART
from time import sleep
import servo

uart = UART(0, tx=Pin(0), rx=Pin(1))
uart.init()
board = servo.KitronikSimplyServos()

board.goToPeriod(0, 1500)
board.goToPeriod(1, 1500)
board.goToPeriod(2, 1500)
board.goToPeriod(3, 1500)
board.goToPeriod(4, 1500)
board.goToPeriod(5, 1500)
board.goToPeriod(6, 1500)
board.goToPeriod(7, 1500)
board.goToPeriod(8, 1500)

#board.goToPeriod(5, 1580)
#board.goToPeriod(6, 1580)
board.goToPeriod(5, 1380)
board.goToPeriod(6, 1380)
sleep(10)
uart.read()

while True:
    if uart.any() :
        if 'x' in uart.read() :
            board.goToPeriod(5, 1500)
            board.goToPeriod(6, 1500)

board.goToPeriod(0, 1500)
board.goToPeriod(1, 1500)
board.goToPeriod(2, 1500)
board.goToPeriod(3, 1500)
board.goToPeriod(4, 1500)
board.goToPeriod(5, 1500)
board.goToPeriod(6, 1500)
board.goToPeriod(7, 1500)
board.goToPeriod(8, 1500)
