# =========================================================
# Nama Fail   : happy_birthday.py
# Fungsi      : Memainkan lagu Happy Birthday menggunakan passive buzzer.
# Papan       : Maker Pi RP2040
# Bahasa      : CircuitPython
# Komponen    : Buzzer onboard / passive buzzer
# Pin Diguna  : Buzzer: GP22
# Tahap       : Sederhana
# Nota        : 
# =========================================================

import time
import board
import pwmio

# Passive buzzer pada GP22
piezo = pwmio.PWMOut(board.GP22, duty_cycle=0, frequency=440, variable_frequency=True)

# Define musical notes (frequencies in Hz)
NOTE_C4 = 262
NOTE_D4 = 294
NOTE_E4 = 330
NOTE_F4 = 349
NOTE_G4 = 392
NOTE_A4 = 440
NOTE_B4 = 494

NOTE_C5 = 523
NOTE_D5 = 587
NOTE_E5 = 659
NOTE_F5 = 698
NOTE_G5 = 784

# Melody: Happy Birthday
melody = [
    NOTE_G4, NOTE_G4, NOTE_A4, NOTE_G4, NOTE_C5, NOTE_B4,
    NOTE_G4, NOTE_G4, NOTE_A4, NOTE_G4, NOTE_D5, NOTE_C5,
    NOTE_G4, NOTE_G4, NOTE_G5, NOTE_E5, NOTE_C5, NOTE_B4, NOTE_A4,
    NOTE_F5, NOTE_F5, NOTE_E5, NOTE_C5, NOTE_D5, NOTE_C5
]

# Note durations
durations = [
    8, 8, 4, 4, 4, 2,
    8, 8, 4, 4, 4, 2,
    8, 8, 4, 4, 4, 4, 2,
    8, 8, 4, 4, 4, 2
]

def play_tone(frequency, duration):
    if frequency == 0:
        piezo.duty_cycle = 0
    else:
        piezo.frequency = frequency
        piezo.duty_cycle = 32768  # 50% duty cycle
    time.sleep(duration)
    piezo.duty_cycle = 0
    time.sleep(0.02)  # gap kecil antara not

print("Happy Birthday!")
for i in range(len(melody)):
    note_duration = 2.0 / durations[i]   # tempo
    play_tone(melody[i], note_duration)

print("Done!")
