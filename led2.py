import board
import digitalio
import time

led0 = digitalio.DigitalInOut(board.GP0)
led1 = digitalio.DigitalInOut(board.GP1)
led0.direction = digitalio.Direction.OUTPUT
led1.direction = digitalio.Direction.OUTPUT

while True:
    led0.value = True
    led1.value = True # Kedua-dua hidup serentak
    time.sleep(0.5)
    led0.value = False
    led1.value = False # Kedua-dua mati serentak
    time.sleep(0.5)