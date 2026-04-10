# =========================================================
# Nama Fail   : doraemon.py
# Fungsi      : Memainkan lagu Doraemon menggunakan buzzer dan NeoPixel sebagai indikator.
# Papan       : Maker Pi RP2040
# Bahasa      : CircuitPython
# Komponen    : Buzzer onboard, NeoPixel onboard
# Pin Diguna  : Buzzer: GP22; NeoPixel: GP18
# Tahap       : Sederhana
# Nota        : Memerlukan modul neopixel_write. Warna NeoPixel mungkin perlu dilaras jika susunan warna board ialah GRB.
# =========================================================

# ============================================
# CircuitPython Buzzer Melody with NeoPixel
# For Maker Pi Pico / Maker Pi RP2040
# ============================================

import board
import time
import pwmio
import digitalio
from neopixel_write import neopixel_write

# ============================================
# TONES DICTIONARY
# Letak terus dalam kod, tidak perlu pitches.py
# ============================================
tones = {
    "": 0,
    "a2": 110,
    "b2": 123,
    "cs3": 139,
    "d3": 147,
    "e3": 165,
    "fs3": 185,
    "g3": 196,
    "a3": 220,
    "b3": 247,
    "cs4": 277,
    "d4": 294,
    "e4": 330,
    "fs4": 370,
    "g4": 392,
    "gs4": 415,
    "a4": 440,
    "b4": 494,
    "cs5": 554,
}

# ============================================
# NEOPIXEL COLOURS
# Perhatian: sesetengah board guna susunan GRB
# ============================================
pixel_off   = bytearray([0, 0, 0])
pixel_red   = bytearray([0, 10, 0])
pixel_green = bytearray([10, 0, 0])
pixel_blue  = bytearray([0, 0, 10])

# ============================================
# NEOPIXEL SETUP
# GP18 biasanya NeoPixel onboard untuk Maker Pi Pico
# ============================================
pixel_pin = digitalio.DigitalInOut(board.GP18)
pixel_pin.direction = digitalio.Direction.OUTPUT

# ============================================
# BUZZER SETUP
# GP22 biasanya buzzer onboard untuk Maker Pi Pico
# ============================================
beeper = pwmio.PWMOut(
    board.GP22,
    duty_cycle=0,
    frequency=440,
    variable_frequency=True
)

# ============================================
# START INDICATOR
# ============================================
neopixel_write(pixel_pin, pixel_green)
time.sleep(1)

tempo = 0.65

melody = (
    'a2','','a2','','a2','b2','','cs3',
    'a3','','d4','d4','','fs4','b4','','fs4','a4','',
    'a4','','b4','a4','','fs4','g4','','fs4','e4','',
    'b3','','e4','e4','','g4','cs5','','cs5','b4','',
    'a4','g4','','g4','','fs4','b3','','cs4','','d4','e4','',

    'a2','','a2','','a2','b2','','cs3',
    'a3','','d4','d4','','fs4','b4','','fs4','a4','',
    'a4','','b4','a4','','fs4','g4','','fs4','e4','',
    'b3','','e4','e4','','g4','cs5','','b4','','a4',
    'g4','','g4','fs4','','e4','cs4','','e4','','d4','',

    'd3','','e3','','fs3','',
    'b4','','b4','','a4','g4','a4','b4','a4','',
    'e4','','fs4','gs4','','e4','a4','',
    'b4','','a4','','e4','','fs4','gs4','','e4','a4','',

    'a2','','a3','','a2','',
    'b4','','a4','','g4','',
    'e4','','cs5','','b4','a4','','b4','a4','','g4','',
    'a4','','b4','fs4','','','e4','d4','',

    'd3','','e3','','fs3','',
    'b4','','a4','','g4','',
    'e4','','cs5','','b4','a4','','b4','a4','','g4','',
    'a4','','b4','fs4','','','e4','d4','',
)

rhythm = [
    4,2,4,4,4,4,4,4,
    4,4,4,4,4,4,4,4,4,4,2,
    4,4,4,4,4,4,4,4,4,4,2,
    4,4,4,4,4,4,4,4,4,4,4,
    4,4,2,4,4,4,4,4,4,2,4,2,4,

    4,2,4,4,4,4,4,4,
    4,4,4,4,4,4,4,4,4,4,2,
    4,4,4,4,4,4,4,4,4,4,2,
    4,4,4,4,4,4,4,2,4,4,4,
    4,4,4,4,4,4,4,2,4,2,2,4,

    4,2,4,2,4,2,
    4,2,4,4,4,4,4,4,4,2,
    4,4,4,4,4,4,2,1,
    4,2,4,2,4,4,4,4,4,4,2,4,

    4,2,4,2,4,2,
    4,2,4,2,2,1,
    4,2,4,4,4,4,4,4,4,4,2,2,
    4,4,4,2,2,4,4,2,4,

    4,2,4,2,4,2,
    4,2,4,2,2,1,
    4,2,4,4,4,4,4,4,4,4,2,2,
    4,4,4,2,2,4,4,2,4,
]

# ============================================
# SAFETY CHECK
# ============================================
if len(melody) != len(rhythm):
    raise ValueError("Panjang melody dan rhythm tidak sama")

# ============================================
# PLAY FUNCTION
# ============================================
def play_song():
    for note, length in zip(melody, rhythm):
        duration = tempo / length

        if note != "" and tones.get(note, 0) > 0:
            neopixel_write(pixel_pin, pixel_red)
            beeper.frequency = tones[note]
            beeper.duty_cycle = 32768   # 50% duty cycle
        else:
            neopixel_write(pixel_pin, pixel_blue)
            beeper.duty_cycle = 0       # senyap / rest

        time.sleep(duration)

        # berhenti sekejap antara nota
        beeper.duty_cycle = 0
        neopixel_write(pixel_pin, pixel_blue)
        time.sleep(0.03)

# ============================================
# MAIN LOOP
# ============================================
while True:
    play_song()
    neopixel_write(pixel_pin, pixel_green)
    time.sleep(2)