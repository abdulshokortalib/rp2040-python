# =========================================================
# Nama Fail   : buzzer3.py
# Fungsi      : Memainkan melodi ringkas Do-Re-Mi-Fa-So pada buzzer.
# Papan       : Maker Pi RP2040
# Bahasa      : CircuitPython
# Komponen    : Buzzer onboard
# Pin Diguna  : Buzzer: GP22
# Tahap       : Asas
# Nota        : Memerlukan pwmio dengan variable_frequency=True untuk menukar frekuensi not.
# =========================================================

import board
import pwmio
import time

# Setup buzzer pada GP18
buzzer = pwmio.PWMOut(board.GP22, variable_frequency=True)

melodi = [262, 294, 330, 349, 392] # Do-Re-Mi-Fa-So

for nada in melodi:
    buzzer.frequency = nada
    buzzer.duty_cycle = 32768
    time.sleep(0.3)
    buzzer.duty_cycle = 0
    time.sleep(0.05)
    
    
    
    
    