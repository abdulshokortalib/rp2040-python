# =========================================================
# Nama Fail   : ambulan_motor.py
# Fungsi      : Sistem amaran ambulans dengan kawalan motor, LCD I2C, dua butang, buzzer dan LED.
# Papan       : Maker Pi RP2040
# Bahasa      : CircuitPython
# Komponen    : LCD Grove JHD1802 I2C, buzzer onboard, 2 push button, Grove LED, motor DC
# Pin Diguna  : LCD: SCL=GP1, SDA=GP0, addr=0x3E; Buzzer: GP22; Butang amaran: GP20; Butang stop: GP21; LED: GP5; Motor1: GP8 & GP9
# Tahap       : Lanjutan
# Nota        : Kod semasa menggunakan I2C pada GP1/GP0, berbeza daripada fail LCD lain yang biasa guna GP3/GP2. Jika LCD tidak berfungsi, semak wiring dan keserasian pin.
# =========================================================

import board
import busio
import time
import pwmio
import digitalio

# =========================================================
# LCD GROVE JHD1802
# NOTE:
# Komen asal kata SCL=GP3, SDA=GP2
# Tetapi kod anda sekarang guna GP1, GP0
# Saya kekalkan ikut kod semasa anda.
# Jika LCD tidak keluar, semak semula wiring I2C.
# =========================================================
i2c = busio.I2C(board.GP1, board.GP0)
LCD_ADDR = 0x3E

def send_command(cmd):
    i2c.writeto(LCD_ADDR, bytes([0x80, cmd]))

def send_data(data):
    i2c.writeto(LCD_ADDR, bytes([0x40, ord(data)]))

def lcd_init():
    while not i2c.try_lock():
        pass
    try:
        time.sleep(0.05)
        send_command(0x38)   # 2 lines, 8-bit mode
        time.sleep(0.05)
        send_command(0x0C)   # display ON, cursor OFF
        send_command(0x01)   # clear
        time.sleep(0.05)
    finally:
        i2c.unlock()

def lcd_clear():
    while not i2c.try_lock():
        pass
    try:
        send_command(0x01)
        time.sleep(0.02)
    finally:
        i2c.unlock()

def display_text(text, line=0):
    while not i2c.try_lock():
        pass
    try:
        addr = 0x80 + (0x40 * line)
        send_command(addr)

        text = text[:16]
        for ch in text:
            send_data(ch)

        for _ in range(16 - len(text)):
            send_data(" ")
    finally:
        i2c.unlock()

def lcd_normal():
    lcd_clear()
    display_text("Sistem Normal", 0)
    display_text("Motor 100%", 1)

def lcd_warning():
    lcd_clear()
    display_text("AMARAN!", 0)
    display_text("Kurangkan laju", 1)

def lcd_stop():
    lcd_clear()
    display_text("SISTEM STOP", 0)
    display_text("Motor berhenti", 1)

def lcd_error(msg="Semak wiring"):
    lcd_clear()
    display_text("Ralat Sistem", 0)
    display_text(msg[:16], 1)

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
# GP20 = AMARAN
# GP21 = STOP
# Pull-up dalaman digunakan
# Tekan = False, lepaskan = True
# =========================================================
button_warning = digitalio.DigitalInOut(board.GP20)
button_warning.direction = digitalio.Direction.INPUT
button_warning.pull = digitalio.Pull.UP

button_stop = digitalio.DigitalInOut(board.GP21)
button_stop.direction = digitalio.Direction.INPUT
button_stop.pull = digitalio.Pull.UP

# =========================================================
# GROVE LED
# =========================================================
LED_PIN = board.GP5
led = digitalio.DigitalInOut(LED_PIN)
led.direction = digitalio.Direction.OUTPUT
led.value = False

def led_off():
    led.value = False

# =========================================================
# MOTOR 1
# =========================================================
MOTOR1_A_PIN = board.GP8
MOTOR1_B_PIN = board.GP9

motor1_a = pwmio.PWMOut(MOTOR1_A_PIN, frequency=20000, duty_cycle=0)
motor1_b = pwmio.PWMOut(MOTOR1_B_PIN, frequency=20000, duty_cycle=0)

def motor_stop():
    motor1_a.duty_cycle = 0
    motor1_b.duty_cycle = 0

def motor_forward(duty):
    motor1_a.duty_cycle = duty
    motor1_b.duty_cycle = 0

def motor_reverse(duty):
    motor1_a.duty_cycle = 0
    motor1_b.duty_cycle = duty

def motor_full():
    motor_forward(65535)   # 100%

def motor_half():
    motor_forward(32768)   # 50%

# =========================================================
# MAIN PROGRAM
# =========================================================
try:
    lcd_init()
    lcd_normal()

    buzzer_off()
    led_off()
    motor_full()

    print("Sistem sedia.")
    print("GP20 = AMARAN")
    print("GP21 = STOP")
    print("Normal: Motor 100%")

    siren_state = 0
    last_toggle = time.monotonic()
    siren_interval = 0.3
    warning_active = False
    stop_active = False

    while True:
        warning_pressed = not button_warning.value
        stop_pressed = not button_stop.value

        # =================================================
        # PRIORITI 1: STOP
        # =================================================
        if stop_pressed:
            if not stop_active:
                print("STOP: Sistem dihentikan")
                lcd_stop()
                buzzer_off()
                led_off()
                motor_stop()
                warning_active = False
                stop_active = True

            time.sleep(0.02)
            continue

        # Jika stop dilepaskan, kembali ke mod normal
        if stop_active:
            print("STOP dilepaskan: Sistem kembali normal")
            lcd_normal()
            buzzer_off()
            led_off()
            motor_full()
            stop_active = False

        # =================================================
        # PRIORITI 2: AMARAN
        # =================================================
        if warning_pressed:
            if not warning_active:
                print("AMARAN: Kurangkan laju")
                lcd_warning()
                motor_half()
                warning_active = True

            now = time.monotonic()
            if now - last_toggle >= siren_interval:
                siren_state = 1 - siren_state
                siren_step(siren_state)

                # LED berkelip ikut siren
                led.value = not led.value

                last_toggle = now

        else:
            if warning_active:
                print("Sistem kembali normal")
                lcd_normal()
                motor_full()
                warning_active = False

            buzzer_off()
            led_off()

        time.sleep(0.02)

except Exception as e:
    buzzer_off()
    led_off()
    motor_stop()
    print("Ralat:", e)
    try:
        lcd_error("Semak wiring")
    except Exception:
        pass