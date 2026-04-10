import board
import digitalio
import time

# LED guna pin Digital 
led = digitalio.DigitalInOut(board.GP5)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    time.sleep(1)
    led.value = False
    time.sleep(1)
    