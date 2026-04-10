# =========================================================
# Nama Fail   : ambulan.py
# Fungsi      : Sistem amaran ambulans menggunakan LCD I2C, buzzer, butang dan Grove LED.
# Papan       : Maker Pi RP2040
# Bahasa      : CircuitPython
# Komponen    : LCD Grove JHD1802 I2C, buzzer onboard, push button, Grove LED
# Pin Diguna  : LCD: SCL=GP3, SDA=GP2, addr=0x3E; Buzzer: GP22; Butang: GP20; LED: GP5
# Tahap       : Sederhana
# Nota        : Memerlukan library standard CircuitPython: board, busio, time, pwmio, digitalio. LCD menggunakan I2C alamat 0x3E.
# =========================================================

import board
import busio
import time
import pwmio
import digitalio

# =========================================================
# LCD GROVE JHD1802
# =========================================================
i2c = busio.I2C(board.GP3, board.GP2)
LCD_ADDR = 0x3E

def send_command(cmd):
    i2c.writeto(LCD_ADDR, bytes([0x80, cmd]))

def send_data(data):
    i2c.writeto(LCD_ADDR, bytes([0x40, ord(data)]))

def lcd_init():
    while not i2c.try_lock():
        pass

    time.sleep(0.05)

    send_command(0x38)
    time.sleep(0.05)

    send_command(0x0C)
    send_command(0x01)

    time.sleep(0.05)

    i2c.unlock()

def lcd_clear():
    while not i2c.try_lock():
        pass

    send_command(0x01)
    time.sleep(0.02)

    i2c.unlock()

def display_text(text, line=0):

    while not i2c.try_lock():
        pass

    addr = 0x80 + (0x40 * line)

    send_command(addr)

    text = text[:16]

    for char in text:
        send_data(char)

    for _ in range(16-len(text)):
        send_data(" ")

    i2c.unlock()

def lcd_normal():

    lcd_clear()
    display_text("Sistem Normal",0)
    display_text("Tekan butang",1)

def lcd_warning():

    lcd_clear()
    display_text("AMARAN!",0)
    display_text("Kurangkan laju",1)

# =========================================================
# BUZZER
# =========================================================
buzzer = pwmio.PWMOut(
    board.GP22,
    duty_cycle=0,
    frequency=1000,
    variable_frequency=True
)

def buzzer_off():
    buzzer.duty_cycle = 0

def siren_step(state):

    buzzer.duty_cycle = 32768

    if state == 0:
        buzzer.frequency = 1000
    else:
        buzzer.frequency = 2000

# =========================================================
# BUTANG
# =========================================================
button = digitalio.DigitalInOut(board.GP20)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

# =========================================================
# GROVE LED
# =========================================================
led = digitalio.DigitalInOut(board.GP5)
led.direction = digitalio.Direction.OUTPUT
led.value = False

# =========================================================
# MAIN PROGRAM
# =========================================================
try:

    lcd_init()
    lcd_normal()

    buzzer_off()
    led.value = False

    print("Sistem sedia.")

    siren_state = 0
    last_toggle = time.monotonic()
    siren_interval = 0.3
    warning_active = False

    while True:

        button_pressed = not button.value

        if button_pressed:

            if not warning_active:

                print("AMARAN: Kurangkan laju")

                lcd_warning()
                warning_active = True

            now = time.monotonic()

            if now - last_toggle >= siren_interval:

                # Tukar state siren
                siren_state = 1 - siren_state

                # Bunyi siren
                siren_step(siren_state)

                # LED berkelip ikut siren
                led.value = not led.value

                last_toggle = now

        else:

            if warning_active:

                print("Sistem kembali normal")

                lcd_normal()
                warning_active = False

            buzzer_off()
            led.value = False

        time.sleep(0.02)

except Exception as e:

    buzzer_off()
    led.value = False

    print("Ralat:", e)