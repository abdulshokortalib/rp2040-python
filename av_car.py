# =========================================================
# Nama Fail   : av_car.py
# Fungsi      : Simulasi kereta autonomi ringkas menggunakan motor DC, sensor ultrasonik dan LCD I2C.
# Papan       : Maker Pi RP2040
# Bahasa      : CircuitPython
# Komponen    : Motor DC, sensor ultrasonik 1-pin, LCD Grove JHD1802 I2C
# Pin Diguna  : Motor1: GP8 & GP9; Ultrasonik SIG: GP1; LCD: SCL=GP3, SDA=GP2, addr=0x3E
# Tahap       : Lanjutan
# Nota        : Memerlukan library adafruit_motor.motor dan modul pulseio. Sensor ultrasonik menggunakan satu pin SIG untuk trigger dan echo.
# =========================================================

import time
import board
import pwmio
import pulseio
import digitalio
import busio
from adafruit_motor import motor

# --- 2. DECLARATION ---

# Motor Tayar Kereta Tok Dalang
m1a = pwmio.PWMOut(board.GP8, frequency=10000)
m1b = pwmio.PWMOut(board.GP9, frequency=10000)
tt_motor = motor.DCMotor(m1a, m1b)

# Sensor Mata Rembo (Ultrasonic)
SIG_PIN = board.GP1

# LCD I2C Dua Seringgit
i2c = busio.I2C(board.GP3, board.GP2)   # SCL, SDA
LCD_ADDR = 0x3E


# =====================================================
# FUNGSI LCD (Skrin Paparan)
# =====================================================
def send_command(cmd):
    i2c.writeto(LCD_ADDR, bytes([0x80, cmd]))

def send_data(ch):
    i2c.writeto(LCD_ADDR, bytes([0x40, ord(ch)]))

def lcd_init():
    while not i2c.try_lock():
        pass
    try:
        time.sleep(0.05)
        send_command(0x38)   # 2 line, 8-bit
        time.sleep(0.01)
        send_command(0x0C)   # display ON, cursor OFF
        time.sleep(0.01)
        send_command(0x01)   # clear display
        time.sleep(0.02)
        send_command(0x06)   # entry mode
        time.sleep(0.01)
    finally:
        i2c.unlock()

def display_text(text, line=0):
    while not i2c.try_lock():
        pass
    try:
        addr = 0x80 if line == 0 else 0xC0
        send_command(addr)

        text = (text[:16] + " " * 16)[:16]

        for ch in text:
            send_data(ch)
    finally:
        i2c.unlock()

def clear_lcd():
    while not i2c.try_lock():
        pass
    try:
        send_command(0x01)
        time.sleep(0.02)
    finally:
        i2c.unlock()


# =====================================================
# FUNGSI SENSOR ULTRASONIK
# =====================================================
def read_distance_cm(sig_pin, timeout_s=0.03):
    # Hantar trigger (Bunyi)
    trig = digitalio.DigitalInOut(sig_pin)
    trig.direction = digitalio.Direction.OUTPUT
    trig.value = False
    time.sleep(0.000002)

    trig.value = True
    time.sleep(0.00001)

    trig.value = False
    trig.deinit()

    # Terima echo (Gema Balik)
    pulses = pulseio.PulseIn(sig_pin, maxlen=1, idle_state=False)
    pulses.clear()

    t0 = time.monotonic()
    while len(pulses) == 0 and (time.monotonic() - t0) < timeout_s:
        pass

    if len(pulses) == 0:
        pulses.deinit()
        return None

    pulse_us = pulses[0]
    pulses.deinit()

    return pulse_us * 0.01715


# =====================================================
# MAIN PROGRAM (Kuasa Otak Kereta!)
# =====================================================
lcd_init()
clear_lcd()
display_text("SISTEM MOTOR", 0)
display_text("SEDANG MULA...", 1)
time.sleep(2)

print("=== Sistem Motor + Sensor + LCD Bermula ===")

try:
    while True:
        d = read_distance_cm(SIG_PIN)

        if d is not None and d > 20:
            tt_motor.throttle = 0.5
            line1 = "JARAK:{:.1f}CM".format(d)
            line2 = "MOTOR: JALAN"
            print("Jarak: {:.1f} cm -> Motor jalan (Selamat!)".format(d))

        else:
            tt_motor.throttle = 0.0

            if d is None:
                line1 = "JARAK: TIADA"
                line2 = "MOTOR: STOP"
                print("Tiada bacaan -> Motor berhenti")
            else:
                line1 = "JARAK REMBO!:{:.1f}CM".format(d)
                line2 = "MOTOR: STOP"
                print("Jarak: {:.1f} cm -> Motor berek mengejut! Ada halangan".format(d))

        display_text(line1, 0)
        display_text(line2, 1)

        time.sleep(0.1)

except Exception as e:
    tt_motor.throttle = 0.0
    clear_lcd()
    display_text("RALAT BERLAKU", 0)
    display_text(str(e)[:16], 1)
    print("Alamak, ralat:", e)

finally:
    tt_motor.throttle = 0.0
    clear_lcd()
    display_text("PROGRAM TAMAT", 0)
    display_text("MOTOR STOP", 1)
    print("Kereta Tok Dalang dimatikan.")
