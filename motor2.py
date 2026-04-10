# code.py (CircuitPython) - Modul 2: Forward & Reverse
import time
import board
import pwmio
from adafruit_motor import motor

M1A_PIN = board.GP8
M1B_PIN = board.GP9
PWM_FREQ = 10000

m1a = pwmio.PWMOut(M1A_PIN, frequency=PWM_FREQ)
m1b = pwmio.PWMOut(M1B_PIN, frequency=PWM_FREQ)
dc_motor = motor.DCMotor(m1a, m1b)

# Forward
print("Forward 0.5")
dc_motor.throttle = 0.5
time.sleep(1.5)

print("Stop")
dc_motor.throttle = 0.0
time.sleep(1.0)

# Reverse
print("Reverse -0.5")
dc_motor.throttle = -0.5
time.sleep(1.5)

print("Stop")
dc_motor.throttle = 0.0

while True:
    time.sleep(1)