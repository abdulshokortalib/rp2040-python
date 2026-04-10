# =========================================================
# Nama Fail   : us2.py
# Fungsi      : Membaca jarak menggunakan sensor ultrasonik dan memaparkan bacaan pada LCD I2C.
# Papan       : Maker Pi RP2040
# Bahasa      : CircuitPython
# Komponen    : Sensor ultrasonik 3-pin (SIG), Grove LCD 16x2 JHD1802 I2C
# Pin Diguna  : GP1 = SIG ultrasonik, GP3 = SCL, GP2 = SDA, alamat I2C = 0x3E
# Tahap       : Sederhana
# Nota        : Menggunakan pulseio, digitalio dan busio. Elakkan konflik pin dengan I2C; fail ini memang mengasingkan ultrasonik pada GP1.
# =========================================================

# Maker Pi RP2040
# Grove 1  -> Ultrasonic Ranger (SIG pada GP1)  <-- tukar jika perlu
# Grove 2  -> Grove LCD 16x2 (JHD1802) I2C: SDA=GP2, SCL=GP3
# I2C address default = 0x3E
#
# Nota penting:
# - LCD guna GP2/GP3, jadi Ultrasonic JANGAN guna GP2/GP3 (elak konflik I2C).
# - Jika Grove 1 anda bukan GP1, tukar ULTRA_PIN sahaja.

import board
import busio
import time
import pulseio
import digitalio

# ==========================
# LCD CONFIGURATION (ikut kod anda)
# ==========================
i2c = busio.I2C(board.GP3, board.GP2)
LCD_ADDR = 0x3E

def send_command(cmd):
    # 0x80 adalah prefix untuk arahan (Command)
    i2c.writeto(LCD_ADDR, bytes([0x80, cmd]))

def send_data(ch):
    # 0x40 adalah prefix untuk data (Karakter)
    i2c.writeto(LCD_ADDR, bytes([0x40, ord(ch)]))

def lcd_init():
    while not i2c.try_lock():
        pass
    time.sleep(0.05)
    send_command(0x38)  # 2 baris, mod 8-bit
    time.sleep(0.05)
    send_command(0x0C)  # Display on, cursor off
    send_command(0x01)  # Clear display
    time.sleep(0.05)
    i2c.unlock()

def display_text(text, line=0):
    # Versi selamat untuk CircuitPython (tanpa .ljust)
    while not i2c.try_lock():
        pass

    # Set cursor position
    addr = 0x80 + (0x40 * line)
    send_command(addr)

    # Maksimum 16 aksara + padding manual
    text = text[:16]
    if len(text) < 16:
        text = text + (" " * (16 - len(text)))

    for char in text:
        send_data(char)

    i2c.unlock()

# ==========================
# ULTRASONIC CONFIGURATION
# ==========================
ULTRA_PIN = board.GP1   # Grove 1 (SIG). Tukar jika Grove 1 anda bukan GP1.

def read_distance_cm(pin, timeout=0.03):
    """
    Baca jarak (cm) dari Grove Ultrasonic Ranger 3-pin (SIG).
    Pulangkan float (cm). Jika gagal/timeout, return None.
    """

    # 1) Trigger pulse 10us
    trig = digitalio.DigitalInOut(pin)
    trig.direction = digitalio.Direction.OUTPUT
    trig.value = False
    time.sleep(0.000002)
    trig.value = True
    time.sleep(0.00001)
    trig.value = False
    trig.deinit()

    # 2) Baca echo pulse (HIGH) menggunakan PulseIn pada pin sama
    pulses = pulseio.PulseIn(pin, maxlen=1, idle_state=False)
    pulses.clear()

    start = time.monotonic()
    while len(pulses) == 0:
        if (time.monotonic() - start) > timeout:
            pulses.deinit()
            return None

    pulse_us = pulses[0]  # microseconds
    pulses.deinit()

    # Convert us -> cm (speed of sound ~34300 cm/s, divide by 2)
    # distance_cm ≈ pulse_us * 0.01715
    return pulse_us * 0.01715

# ==========================
# MAIN PROGRAM
# ==========================
print("Memulakan sistem...")

try:
    lcd_init()
    display_text("Ultrasonic Test", 0)
    display_text("Starting...", 1)
    time.sleep(1.5)

    while True:
        d = read_distance_cm(ULTRA_PIN)

        if d is None:
            display_text("Sensor Error", 0)
            display_text("Check wiring", 1)
            print("Sensor Error / timeout")
        else:
            display_text("Jarak:", 0)
            display_text("{:.1f} cm".format(d), 1)
            print("Jarak: {:.1f} cm".format(d))

        time.sleep(0.3)

except Exception as e:
    print("Ralat:", e)
    # Cuba paparkan ralat ringkas pada LCD
    try:
        display_text("Ralat:", 0)
        display_text(str(e)[:16], 1)
    except:
        pass