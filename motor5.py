# =========================================================
# Nama Fail   : motor5.py
# Fungsi      : Menukar status motor ON/OFF secara toggle menggunakan satu butang.
# Papan       : Maker Pi RP2040
# Bahasa      : CircuitPython
# Komponen    : Motor DC pada saluran M1, 1 butang onboard/luaran
# Pin Diguna  : GP8 = M1A, GP9 = M1B, GP20 = butang input (pull-up)
# Tahap       : Sederhana
# Nota        : Memerlukan library adafruit_motor. Menggunakan debounce ringkas 0.2 saat dan throttle 0.6 apabila motor ON.
# =========================================================

# code.py (CircuitPython) - Modul 5: Toggle motor ON/OFF (GP20)
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

btn = digitalio.DigitalInOut(board.GP20)
btn.direction = digitalio.Direction.INPUT
btn.pull = digitalio.Pull.UP

motor_on = False
last_btn = True

print("Tekan sekali untuk ON, tekan lagi untuk OFF.")

while True:
    now = btn.value

    # Edge detect: perubahan + butang ditekan (LOW)
    if now != last_btn and (not now):
        motor_on = not motor_on
        time.sleep(0.2)  # debounce

    last_btn = now

    dc_motor.throttle = 0.6 if motor_on else 0.0
    time.sleep(0.01)