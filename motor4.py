# code.py (CircuitPython) - Modul 4: Button momentary (GP20)
import time
import board
import pwmio
import digitalio
from adafruit_motor import motor

M1A_PIN = board.GP8
M1B_PIN = board.GP9
PWM_FREQ = 10000

m1a = pwmio.PWMOut(M1A_PIN, frequency=PWM_FREQ)
m1b = pwmio.PWMOut(M1B_PIN, frequency=PWM_FREQ)
dc_motor = motor.DCMotor(m1a, m1b)

# Button on GP20 (Pull-up)
btn = digitalio.DigitalInOut(board.GP20)
btn.direction = digitalio.Direction.INPUT
btn.pull = digitalio.Pull.UP

print("Tekan butang untuk jalan. Lepas untuk stop.")

while True:
    if not btn.value:          # ditekan
        dc_motor.throttle = 0.7
    else:
        dc_motor.throttle = 0.0
    time.sleep(0.01)           # kecilkan beban CPU