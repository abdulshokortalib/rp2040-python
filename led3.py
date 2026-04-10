# =========================================================
# Nama Fail   : led3.py
# Fungsi      : Menghidup dan memadam dua LED secara berselang-seli.
# Papan       : Maker Pi RP2040
# Bahasa      : CircuitPython
# Komponen    : 2 LED digital
# Pin Diguna  : LED0: GP0; LED1: GP1
# Tahap       : Asas
# Nota        : Sesuai untuk latihan asas corak nyalaan LED menggunakan loop dan delay.
# =========================================================

import board
import digitalio
import time

led0 = digitalio.DigitalInOut(board.GP0)
led1 = digitalio.DigitalInOut(board.GP1)
led0.direction = digitalio.Direction.OUTPUT
led1.direction = digitalio.Direction.OUTPUT

while True:
    led0.value = True
    led1.value = False
    time.sleep(0.2)
    led0.value = False
    led1.value = True
    time.sleep(0.2)