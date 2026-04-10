# =========================================================
# Nama Fail   : grovebuzzer3.py
# Fungsi      : Mengawal Grove buzzer dan LED secara serentak sebanyak 2 kali.
# Papan       : Maker Pi RP2040
# Bahasa      : CircuitPython
# Komponen    : Grove buzzer, Grove LED / LED digital
# Pin Diguna  : Buzzer: GP17; LED: GP5
# Tahap       : Asas
# Nota        : Menggunakan variable_frequency=True pada pwmio.PWMOut untuk buzzer.
# =========================================================

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