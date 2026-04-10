import board
import digitalio
import time

led0 = digitalio.DigitalInOut(board.GP0)
led1 = digitalio.DigitalInOut(board.GP1)
led0.direction = digitalio.Direction.OUTPUT
led1.direction = digitalio.Direction.OUTPUT

while True:
    led0.value = True
    led1.value = False
    time.sleep(0.2)
    led0.value = False
    led1.value = True
    time.sleep(0.2)