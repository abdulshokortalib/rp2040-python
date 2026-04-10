# =========================================================
# Nama Fail   : beep.py
# Fungsi      : Membunyikan buzzer sekali untuk ujian asas.
# Papan       : Maker Pi RP2040
# Bahasa      : CircuitPython
# Komponen    : Buzzer onboard
# Pin Diguna  : Buzzer: GP22
# Tahap       : Asas
# Nota        : Menggunakan pwmio.PWMOut tanpa variable_frequency kerana frekuensi tetap 2000 Hz.
# =========================================================

import board
import pwmio
import time

# Buzzer pada Maker Pi RP2040
buzzer = pwmio.PWMOut(board.GP22, duty_cycle=0, frequency=2000)

print("Beep test")

# Hidupkan buzzer
buzzer.duty_cycle = 32768   # 50% duty cycle
time.sleep(0.2)             # bunyi selama 0.2 saat

# Matikan buzzer
buzzer.duty_cycle = 0

print("Beep selesai")