# =========================================================
# Nama Fail   : led5.py
# Fungsi      : Menukar status LED secara toggle menggunakan satu butang pada setiap tekanan.
# Papan       : Maker Pi RP2040
# Bahasa      : CircuitPython
# Komponen    : 2 LED onboard (GP0, GP1), 1 butang onboard/luaran
# Pin Diguna  : GP0 = LED utama toggle, GP1 = LED tambahan diinisialisasi tetapi tidak digunakan dalam logik, GP20 = butang input (pull-up)
# Tahap       : Asas
# Nota        : Menggunakan debounce ringkas melalui time.sleep(0.05). GP1 diinisialisasi tetapi tidak digunakan.
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

led_status = False
last_btn_state = True

while True:
    current_btn_state = btn.value
    if current_btn_state != last_btn_state:
        if not current_btn_state: # Baru ditekan
            led_status = not led_status
            led0.value = led_status
        time.sleep(0.05) # Debounce delay
    last_btn_state = current_btn_state