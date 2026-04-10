# =========================================================
# Nama Fail   : led4.py
# Fungsi      : Mengawal LED secara momentary menggunakan butang; LED menyala hanya semasa butang ditekan.
# Papan       : Maker Pi RP2040
# Bahasa      : CircuitPython
# Komponen    : 2 LED onboard (GP0, GP1), 1 butang onboard/luaran
# Pin Diguna  : GP0 = LED utama, GP1 = LED tambahan diinisialisasi tetapi tidak digunakan dalam logik, GP20 = butang input (pull-up)
# Tahap       : Asas
# Nota        : Menggunakan digitalio dan pull-up dalaman. Fail semasa hanya mengawal GP0; GP1 diinisialisasi tetapi tidak digunakan.
# =========================================================

import board
import digitalio
import time

led0 = digitalio.DigitalInOut(board.GP0)
led1 = digitalio.DigitalInOut(board.GP1)
led0.direction = digitalio.Direction.OUTPUT
led1.direction = digitalio.Direction.OUTPUT

btn = digitalio.DigitalInOut(board.GP20)
btn.direction = digitalio.Direction.INPUT
btn.pull = digitalio.Pull.UP

while True:
    if not btn.value: # Jika butang ditekan (Low)
        led0.value = True
    else:
        led0.value = False