import board
import digitalio
import time

led = digitalio.DigitalInOut(board.GP5)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True # LED Hidup
    time.sleep(1.0) # Tunggu 1 saat
    led.value = False # LED Mati
    time.sleep(1.0) # Tunggu 1 saat# Write your code here :-)
