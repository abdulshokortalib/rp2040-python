# =========================================================
# Nama Fail   : buzzer1.py
# Fungsi      : Menghidup dan memadam LED Grove secara berkelip walaupun nama fail merujuk kepada buzzer.
# Papan       : Maker Pi RP2040
# Bahasa      : CircuitPython
# Komponen    : Grove LED / LED digital
# Pin Diguna  : LED: GP5
# Tahap       : Asas
# Nota        : Nama fail tidak sepadan dengan fungsi sebenar kod. Fail ini tidak menggunakan buzzer.
# =========================================================

import board
import digitalio
import time

# LED guna pin Digital 
led = digitalio.DigitalInOut(board.GP5)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    time.sleep(1)
    led.value = False
    time.sleep(1)
    