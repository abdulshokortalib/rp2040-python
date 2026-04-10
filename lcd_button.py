import board
import busio
import time
import pwmio
import digitalio

# =========================================================
# LCD GROVE JHD1802 (berdasarkan kod yang telah berjaya)
# SDA = GP2, SCL = GP3
# I2C address = 0x3E
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
    try:
        time.sleep(0.05)
        send_command(0x38)   # 2 baris, mod 8-bit
        time.sleep(0.05)
        send_command(0x0C)   # display ON, cursor OFF
        send_command(0x01)   # clear display
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

        # pastikan maksimum 16 aksara
        text = text[:16]
        for char in text:
            send_data(char)

        # pad ruang kosong supaya baki aksara lama hilang
        for _ in range(16 - len(text)):
            send_data(" ")
    finally:
        i2c.unlock()

def lcd_normal():
    lcd_clear()
    display_text("Sistem Normal", 0)
    display_text("Tekan butang", 1)

def lcd_warning():
    lcd_clear()
    display_text("AMARAN!", 0)
    display_text("Kurangkan laju", 1)

def lcd_error(msg="Semak wiring"):
    lcd_clear()
    display_text("Ralat Sistem", 0)
    display_text(msg[:16], 1)

# =========================================================
# BUZZER SIREN
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
    buzzer.duty_cycle = 32768  # lebih kurang 50% duty cycle
    if state == 0:
        buzzer.frequency = 1000
    else:
        buzzer.frequency = 2000

# =========================================================
# BUTANG
# Sambungan:
# satu kaki butang -> GP20
# satu kaki lagi   -> GND
# pull-up dalaman digunakan
# =========================================================
button = digitalio.DigitalInOut(board.GP20)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

# =========================================================
# LED AMARAN
# Jika board anda ada LED terbina dalam pada pin lain,
# tukar sahaja GP18 kepada pin sebenar LED anda.
# =========================================================
led = digitalio.DigitalInOut(board.GP18)
led.direction = digitalio.Direction.OUTPUT
led.value = False

def led_on():
    led.value = True

def led_off():
    led.value = False

# =========================================================
# MAIN PROGRAM
# =========================================================
try:
    lcd_init()
    lcd_normal()
    buzzer_off()
    led_off()

    print("Sistem sedia.")

    siren_state = 0
    last_toggle_time = time.monotonic()
    siren_interval = 0.3
    warning_active = False

    while True:
        # pull-up logic:
        # button.value = True  -> tidak ditekan
        # button.value = False -> ditekan
        button_pressed = not button.value

        if button_pressed:
            if not warning_active:
                print("AMARAN: Kurangkan laju")
                lcd_warning()
                led_on()
                warning_active = True

            now = time.monotonic()
            if now - last_toggle_time >= siren_interval:
                siren_state = 1 - siren_state
                siren_step(siren_state)
                last_toggle_time = now

        else:
            if warning_active:
                print("Sistem kembali normal")
                lcd_normal()
                led_off()
                warning_active = False

            buzzer_off()

        time.sleep(0.02)

except Exception as e:
    buzzer_off()
    led_off()
    print("Ralat:", e)
    try:
        lcd_error("Semak wiring")
    except Exception:
        pass