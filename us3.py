import time
import board
import digitalio
import pulseio
import pwmio
from adafruit_motor import motor

SIG_PIN = board.GP1

def read_distance_cm(sig_pin, timeout_s=0.03):
    trig = digitalio.DigitalInOut(sig_pin)
    trig.direction = digitalio.Direction.OUTPUT
    trig.value = False
    time.sleep(0.000002)
    trig.value = True
    time.sleep(0.000015)
    trig.value = False
    trig.deinit()

    pulses = pulseio.PulseIn(sig_pin, maxlen=1, idle_state=False)
    pulses.clear()
    pulses.resume()

    start = time.monotonic()
    while len(pulses) == 0:
        if time.monotonic() - start > timeout_s:
            pulses.deinit()
            return None

    echo_us = pulses[0]
    pulses.deinit()
    return (echo_us * 0.0343) / 2.0

# Motor M1 (Maker Pi RP2040): GP8 & GP9 (seperti contoh anda)
m1a = pwmio.PWMOut(board.GP8, frequency=10000)
m1b = pwmio.PWMOut(board.GP9, frequency=10000)
tt_motor = motor.DCMotor(m1a, m1b)

while True:
    d = read_distance_cm(SIG_PIN)
    if d is None:
        tt_motor.throttle = 0
        print("Sensor timeout")
    else:
        if d > 30:
            tt_motor.throttle = 0.8   # laju
        elif d > 10:
            tt_motor.throttle = 0.3   # perlahan
        else:
            tt_motor.throttle = 0.0   # henti

        print("Jarak: {:.1f} cm | throttle: {:.1f}".format(d, tt_motor.throttle))

    time.sleep(0.15)