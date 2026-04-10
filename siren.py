# =========================================================
# Nama Fail   : siren.py
# Fungsi      : Menghasilkan bunyi siren dengan menukar frekuensi buzzer antara nada rendah dan tinggi secara berterusan.
# Papan       : Maker Pi RP2040
# Bahasa      : CircuitPython
# Komponen    : Buzzer onboard
# Pin Diguna  : GP22 = buzzer PWM
# Tahap       : Asas
# Nota        : Menggunakan PWMOut dengan variable_frequency=True supaya frekuensi boleh diubah semasa loop.
# =========================================================

# --- 1. PREPARATION ---
import board, pwmio, time

# --- 2. DECLARATION ---
# variable_frequency=True wajib jika mahu ubah frequency semasa loop
buzzer = pwmio.PWMOut(
    board.GP22,
    duty_cycle=0,
    frequency=1000,
    variable_frequency=True
)

# --- 3. EXECUTION ---
try:
    print("Lari! Siren bunyi!")
    
    while True:
        buzzer.duty_cycle = 32768   # Hidupkan bunyi
        buzzer.frequency = 1000     # Nada rendah
        time.sleep(0.3)

        buzzer.frequency = 2000     # Nada tinggi
        time.sleep(0.3)

# --- 4. TERMINATION ---
except Exception as e:
    print("Brek kecemasan:", e)
    buzzer.duty_cycle = 0          # Matikan bunyi jika ralat