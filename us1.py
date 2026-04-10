# =========================================================
# Nama Fail   : us1.py
# Fungsi      : Mengelipkan LED pada GP5 secara berterusan.
# Papan       : Maker Pi RP2040
# Bahasa      : CircuitPython
# Komponen    : LED onboard/Grove LED
# Pin Diguna  : GP5 = LED output
# Tahap       : Asas
# Nota        : Nama fail mencadangkan ultrasonic, tetapi kandungan sebenar fail ini hanyalah contoh LED blink.
# =========================================================

# --- 1. PREPARATION (Persediaan Library) ---
import board
import digitalio
import time

# --- 2. DECLARATION (Pengenalan Pin) ---
led = digitalio.DigitalInOut(board.GP5)
led.direction = digitalio.Direction.OUTPUT

# --- 3. EXECUTION (Jalankan Pengekodan) ---
try:
    print("Mari mula kelipkan lampu!")
    while True:
        led.value = True      # Lampu ON
        time.sleep(1.0)       # Tunggu 1 saat
        led.value = False     # Lampu OFF
        time.sleep(1.0)       # Tunggu 1 saat

# --- 4. TERMINATION (Penamatan) ---
except Exception as e:
    print("Ada ralat lah:", e)
