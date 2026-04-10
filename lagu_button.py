import board
import time
import pwmio
import digitalio
from neopixel_write import neopixel_write

# =========================================================
# MAKER PI RP2040 BUZZER PLAYER
# GP20 -> Doraemon
# GP21 -> Happy Birthday
# =========================================================

print("\n==============================")
print("Maker Pi RP2040 Music Player")
print("==============================")
print("Tekan butang untuk memainkan lagu")
print("GP20 -> Doraemon")
print("GP21 -> Happy Birthday")
print("Menunggu input...\n")

# =========================================================
# TONES DICTIONARY
# =========================================================
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
    "as4": 466,
    "b4": 494,
    "c5": 523,
    "cs5": 554,
    "d5": 587,
    "e5": 659,
    "f5": 698,
    "g5": 784,
}

# =========================================================
# NEOPIXEL COLOUR
# =========================================================
pixel_off    = bytearray([0, 0, 0])
pixel_red    = bytearray([0, 10, 0])
pixel_green  = bytearray([10, 0, 0])
pixel_blue   = bytearray([0, 0, 10])
pixel_yellow = bytearray([10, 10, 0])

pixel_pin = digitalio.DigitalInOut(board.GP18)
pixel_pin.direction = digitalio.Direction.OUTPUT

def set_pixel(color):
    neopixel_write(pixel_pin, color)

# =========================================================
# BUZZER
# =========================================================
beeper = pwmio.PWMOut(
    board.GP22,
    duty_cycle=0,
    frequency=440,
    variable_frequency=True
)

# =========================================================
# BUTTON
# =========================================================
btn_doraemon = digitalio.DigitalInOut(board.GP20)
btn_doraemon.direction = digitalio.Direction.INPUT
btn_doraemon.pull = digitalio.Pull.UP

btn_birthday = digitalio.DigitalInOut(board.GP21)
btn_birthday.direction = digitalio.Direction.INPUT
btn_birthday.pull = digitalio.Pull.UP

# =========================================================
# START INDICATOR
# =========================================================
set_pixel(pixel_green)
time.sleep(1)

# =========================================================
# DORAEMON DATA
# =========================================================
tempo_doraemon = 0.65

melody_doraemon = (
'a2','','a2','','a2','b2','','cs3',
'a3','','d4','d4','','fs4','b4','','fs4','a4','',
'a4','','b4','a4','','fs4','g4','','fs4','e4','',
'b3','','e4','e4','','g4','cs5','','cs5','b4','',
'a4','g4','','g4','','fs4','b3','','cs4','','d4','e4','',
)

rhythm_doraemon = [
4,2,4,4,4,4,4,4,
4,4,4,4,4,4,4,4,4,4,2,
4,4,4,4,4,4,4,4,4,4,2,
4,4,4,4,4,4,4,4,4,4,4,
4,4,2,4,4,4,4,4,4,2,4,2,4
]

# =========================================================
# HAPPY BIRTHDAY
# =========================================================
tempo_birthday = 0.8

melody_birthday = [
"c5","c5","d5","c5","f5","e5",
"c5","c5","d5","c5","g5","f5",
"c5","c5","c5","a4","f5","e5","d5",
"as4","as4","a4","f5","g5","f5"
]

rhythm_birthday = [
4,4,2,2,2,1,
4,4,2,2,2,1,
4,4,2,2,2,2,1,
4,4,2,2,2,1
]

# =========================================================
# PLAY NOTE
# =========================================================
def play_note(note, duration):

    if note != "" and tones.get(note,0) > 0:
        set_pixel(pixel_red)
        beeper.frequency = tones[note]
        beeper.duty_cycle = 32768
    else:
        set_pixel(pixel_blue)
        beeper.duty_cycle = 0

    time.sleep(duration)

    beeper.duty_cycle = 0
    set_pixel(pixel_blue)
    time.sleep(0.03)

# =========================================================
# PLAY SONG FUNCTIONS
# =========================================================
def play_doraemon():

    print(">> Lagu Doraemon dimainkan")

    for note, length in zip(melody_doraemon, rhythm_doraemon):
        duration = tempo_doraemon / length
        play_note(note, duration)

    print(">> Tamat Doraemon\n")

def play_birthday():

    print(">> Lagu Happy Birthday dimainkan")

    for note, length in zip(melody_birthday, rhythm_birthday):
        duration = tempo_birthday / length
        play_note(note, duration)

    print(">> Tamat Happy Birthday\n")

# =========================================================
# WAIT RELEASE
# =========================================================
def wait_release(button):
    while not button.value:
        time.sleep(0.02)

# =========================================================
# MAIN LOOP
# =========================================================
while True:

    if not btn_doraemon.value:
        play_doraemon()
        wait_release(btn_doraemon)

    elif not btn_birthday.value:
        play_birthday()
        wait_release(btn_birthday)

    time.sleep(0.02)