import board
import digitalio
import time

led0 = digitalio.DigitalInOut(board.GP0)
led1 = digitalio.DigitalInOut(board.GP1)
led0.direction = digitalio.Direction.OUTPUT
led1.direction = digitalio.Direction.OUTPUT

btn = digitalio.DigitalInOut(board.GP20)
btn.direction = digitalio.Direction.INPUT
btn.pull = digitalio.Pull.UP

led_status = False
last_btn_state = True

while True:
    current_btn_state = btn.value
    if current_btn_state != last_btn_state:
        if not current_btn_state: # Baru ditekan
            led_status = not led_status
            led0.value = led_status
        time.sleep(0.05) # Debounce delay
    last_btn_state = current_btn_state