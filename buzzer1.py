# =========================================================
# Nama Fail   : buzzer1.py
# Fungsi      : Menghidup dan memadam buzzer.
# Papan       : Maker Pi RP2040
# Bahasa      : CircuitPython
# Komponen    : On Board Buzzer /Grove Buzzer
# Pin Diguna  : Buzzer: GP22
# Tahap       : Asas
# Nota        : 
# =========================================================

import board
import pwmio
import time
import digitalio

buzzer = pwmio.PWMOut(board.GP22, variable_frequency=True)

for i in range(3):
    buzzer.duty_cycle = 32768
    time.sleep(0.2)
    buzzer.duty_cycle = 0
    time.sleep(0.2)
    
