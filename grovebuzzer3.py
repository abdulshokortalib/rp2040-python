import board
import pwmio
import time
import digitalio

led = digitalio.DigitalInOut(board.GP5)
led.direction = digitalio.Direction.OUTPUT

# Setup buzzer pada GP18
buzzer = pwmio.PWMOut(board.GP17, variable_frequency=True)

for i in range(2):
    buzzer.duty_cycle = 32768
    led.value = True
    time.sleep(0.2)
    buzzer.duty_cycle = 0
    led.value = False
    time.sleep(0.2)