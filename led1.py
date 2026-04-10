# =========================================================
# Nama Fail   : led1.py
# Fungsi      : Menghidup dan memadam satu LED secara berkelip.
# Papan       : Maker Pi RP2040
# Bahasa      : CircuitPython
# Komponen    : LED digital
# Pin Diguna  : LED: GP0
# Tahap       : Asas
# Nota        : Kod menggunakan while True. Baris komentar akhir “Write your code here :-)” boleh dibuang untuk kemasan.
# =========================================================

import board
import digitalio
import time

led = digitalio.DigitalInOut(board.GP0)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True # LED Hidup
    time.sleep(1.0) # Tunggu 1 saat
    led.value = False # LED Mati
    time.sleep(1.0) # Tunggu 1 saat# Write your code here :-)
