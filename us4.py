# =========================================================
# Nama Fail   : us4.py
# Fungsi      : Membaca jarak ultrasonik, memaparkan nilai pada LCD, dan melaras kelajuan motor secara automatik.
# Papan       : Maker Pi RP2040
# Bahasa      : CircuitPython
# Komponen    : Sensor ultrasonik 3-pin (SIG), Grove LCD 16x2 JHD1802 I2C, motor DC pada saluran M1
# Pin Diguna  : GP1 = SIG ultrasonik, GP3 = SCL, GP2 = SDA, GP8 = M1A, GP9 = M1B, alamat I2C = 0x3E
# Tahap       : Lanjutan
# Nota        : Memerlukan library adafruit_motor. Menggabungkan sensor, LCD dan motor dalam satu sistem kawalan asas.
# =========================================================

import time
import board
import digitalio
import pulseio
import busio
import pwmio
from adafruit_motor import motor

# ==========================
# KONFIGURASI PIN & PERANTI
# ==========================
# LCD pada Grove 2 (SDA=GP2, SCL=GP3)
# Ultrasonic pada Grove 1 (SIG=GP1)
# Motor M1 pada GP8 & GP9
ULTRA_PIN = board.GP1
I2C_SDA = board.GP2
I2C_SCL = board.GP3
LCD_ADDR = 0x3E

# Setup I2C untuk LCD
i2c = busio.I2C(I2C_SCL, I2C_SDA)

# Setup Motor M1
m1a = pwmio.PWMOut(board.GP8, frequency=10000)
m1b = pwmio.PWMOut(board.GP9, frequency=10000)
tt_motor = motor.DCMotor(m1a, m1b)

# ==========================
# FUNGSI LCD (Low-Level)
# ==========================
def send_command(cmd):
    i2c.writeto(LCD_ADDR, bytes([0x80, cmd]))

def send_data(ch):
    i2c.writeto(LCD_ADDR, bytes([0x40, ord(ch)]))

def lcd_init():
    while not i2c.try_lock(): pass
    time.sleep(0.05)
    send_command(0x38) # 2 baris, mod 8-bit
    send_command(0x0C) # Display on
    send_command(0x01) # Clear display
    time.sleep(0.05)
    i2c.unlock()

def display_text(text, line=0):
    while not i2c.try_lock(): pass
    addr = 0x80 + (0x40 * line)
    send_command(addr)
    # Pastikan 16 aksara (tambah space jika pendek)
    text = (text[:16] + " " * 16)[:16]
    for char in text:
        send_data(char)
    i2c.unlock()

# ==========================
# FUNGSI ULTRASONIC
# ==========================
def read_distance_cm(pin, timeout=0.03):
    # Trigger pulse
    trig = digitalio.DigitalInOut(pin)
    trig.direction = digitalio.Direction.OUTPUT
    trig.value = False
    time.sleep(0.000002)
    trig.value = True
    time.sleep(0.00001)
    trig.value = False
    trig.deinit()

    # Echo pulse
    pulses = pulseio.PulseIn(pin, maxlen=1, idle_state=False)
    start = time.monotonic()
    while len(pulses) == 0:
        if (time.monotonic() - start) > timeout:
            pulses.deinit()
            return None
    
    pulse_us = pulses[0]
    pulses.deinit()
    return pulse_us * 0.01715

def clamp(x, lo, hi):
    return lo if x < lo else hi if x > hi else x

# ==========================
# MAIN LOOP
# ==========================
lcd_init()
display_text("AI Autonomous", 0)
display_text("Starting...", 1)
time.sleep(1.0)

while True:
    d = read_distance_cm(ULTRA_PIN)
    
    if d is None:
        tt_motor.throttle = 0
        display_text("Sensor Error", 0)
        display_text("Check Wiring", 1)
    else:
        # Logik Kelajuan (Mapping)
        if d <= 10:
            speed = 0.0
        else:
            # Contoh: Jarak 50cm ke atas = Speed 1.0 (Full)
            speed = (d - 10) / 40.0
            speed = clamp(speed, 0.0, 1.0)
        
        tt_motor.throttle = speed
        
        # Paparan LCD yang lebih kemas
        display_text("Dist: {:.1f}cm".format(d), 0)
        display_text("Speed: {:.2f}".format(speed), 1)

    time.sleep(0.1) # Respon lebih pantas untuk elak langgar dinding