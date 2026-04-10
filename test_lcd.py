# Maker Pi RP2040 + Grove 16x2 LCD (JHD1802) I2C Tester
# Wiring (ikut halaman anda):
#   SDA = GP2, SCL = GP3
# I2C address default = 0x3E
import board
import busio
import time

# Inisialisasi I2C pada Maker Pi RP2040 (Port Grove GP2/GP3)
i2c = busio.I2C(board.GP3, board.GP2)

# Alamat I2C untuk Grove LCD (JHD1802)
LCD_ADDR = 0x3E

def send_command(cmd):
    # 0x80 adalah prefix untuk arahan (Command)
    i2c.writeto(LCD_ADDR, bytes([0x80, cmd]))

def send_data(data):
    # 0x40 adalah prefix untuk data (Karakter)
    i2c.writeto(LCD_ADDR, bytes([0x40, ord(data)]))

def lcd_init():
    while not i2c.try_lock():
        pass
    time.sleep(0.05)
    send_command(0x38) # 2 baris, mod 8-bit
    time.sleep(0.05)
    send_command(0x0C) # Display on, cursor off
    send_command(0x01) # Clear display
    time.sleep(0.05)
    i2c.unlock()

def display_text(text, line=0):
    if not i2c.try_lock():
        return
    # Set cursor position
    addr = 0x80 + (0x40 * line)
    send_command(addr)
    for char in text:
        send_data(char)
    i2c.unlock()

# --- Main Program ---
try:
    lcd_init()
    display_text("Hello World,", 0)
    display_text("Are you ready?", 1)
    print("Berjaya dipaparkan!")
except Exception as e:
    print(f"Ralat: {e}")


