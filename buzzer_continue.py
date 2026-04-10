# =========================================================
# Nama Fail   : buzzer_continue.py
# Fungsi      : Membunyikan buzzer secara berterusan dengan sela masa tetap.
# Papan       : Maker Pi RP2040
# Bahasa      : CircuitPython
# Komponen    : Buzzer onboard
# Pin Diguna  : Buzzer: GP22
# Tahap       : Asas
# Nota        : Kod menggunakan while True, jadi bunyi akan berulang tanpa henti sehingga papan dihentikan.
# =========================================================

import board
import pwmio
import time

# Setup buzzer (Maker Pi RP2040 biasanya GP22)
buzzer = pwmio.PWMOut(board.GP22, duty_cycle=0, frequency=2000)

print("Beep berterusan bermula")

while True:

    # Bunyi ON
    buzzer.duty_cycle = 32768
    time.sleep(0.2)

    # Bunyi OFF
    buzzer.duty_cycle = 0
    time.sleep(0.5)