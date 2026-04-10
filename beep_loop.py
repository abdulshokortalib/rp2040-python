# =========================================================
# Nama Fail   : beep_loop.py
# Fungsi      : Membunyikan buzzer sebanyak 3 kali secara berulang.
# Papan       : Maker Pi RP2040
# Bahasa      : CircuitPython
# Komponen    : Buzzer onboard
# Pin Diguna  : Buzzer: GP22
# Tahap       : Asas
# Nota        : Sesuai untuk latihan asas loop dan kawalan buzzer menggunakan pwmio.
# =========================================================

import board
import pwmio
import time

# Setup buzzer (Maker Pi RP2040 biasanya GP22)
buzzer = pwmio.PWMOut(board.GP22, duty_cycle=0, frequency=2000)

print("Beep 3 kali bermula")

# Loop 3 kali
for i in range(3):

    buzzer.duty_cycle = 32768   # ON (50% duty cycle)
    time.sleep(0.2)             # bunyi 0.2 saat

    buzzer.duty_cycle = 0       # OFF
    time.sleep(0.2)             # jeda sebelum beep seterusnya

print("Beep selesai")