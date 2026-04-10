# =========================================================
# Nama Fail   : motor1.py
# Fungsi      : Menggerakkan motor DC ke arah hadapan selama 2 saat kemudian berhenti.
# Papan       : Maker Pi RP2040
# Bahasa      : CircuitPython
# Komponen    : Motor DC pada saluran M1, driver motor onboard
# Pin Diguna  : GP8 = M1A, GP9 = M1B
# Tahap       : Asas
# Nota        : Memerlukan library adafruit_motor. Kod mengekalkan program hidup dengan gelung while True selepas motor berhenti.
# =========================================================

# code.py (CircuitPython) - Modul 1: Forward 2s kemudian berhenti
import time
import board
import pwmio
from adafruit_motor import motor

# ===== Tetapan Motor 1 (Maker Pi RP2040)
# Motor 1 biasanya: GP8 (A) dan GP9 (B)
M1A_PIN = board.GP8
M1B_PIN = board.GP9
PWM_FREQ = 10000  # 10kHz (sesuai untuk motor DC kecil)

m1a = pwmio.PWMOut(M1A_PIN, frequency=PWM_FREQ)
m1b = pwmio.PWMOut(M1B_PIN, frequency=PWM_FREQ)
dc_motor = motor.DCMotor(m1a, m1b)

print("Motor forward 2 saat...")
dc_motor.throttle = 1.0     # forward penuh
time.sleep(2.0)

print("Motor stop")
dc_motor.throttle = 0.0     # stop

# Kekal hidup (supaya code.py tak tamat)
while True:
    time.sleep(1)