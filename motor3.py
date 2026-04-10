# code.py (CircuitPython) - Modul 3: Ramp speed (PWM)
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

speeds = [0.2, 0.4, 0.6, 0.8, 1.0]

print("Ramp speed...")
for s in speeds:
    print("Throttle:", s)
    dc_motor.throttle = s
    time.sleep(0.5)

print("Stop")
dc_motor.throttle = 0.0

while True:
    time.sleep(1)