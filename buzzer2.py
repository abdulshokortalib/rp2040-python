# =========================================================
# Nama Fail   : buzzer2.py
# Fungsi      : Mengawal buzzer dan LED secara serentak sebanyak 2 kali.
# Papan       : Maker Pi RP2040
# Bahasa      : CircuitPython
# Komponen    : Buzzer onboard, LED digital
# Pin Diguna  : Buzzer: GP22; LED: GP0
# Tahap       : Asas
# Nota        : Komen asal menyebut GP18 tetapi kod sebenar menggunakan GP22 untuk buzzer.
# =========================================================

import board
import pwmio
import time
import digitalio

led = digitalio.DigitalInOut(board.GP0)
led.direction = digitalio.Direction.OUTPUT

# Setup buzzer pada GP18
buzzer = pwmio.PWMOut(board.GP22, variable_frequency=True)

for i in range(2):
    buzzer.duty_cycle = 32768
    led.value = True
    time.sleep(0.2)
    buzzer.duty_cycle = 0
    led.value = False
    time.sleep(0.2)