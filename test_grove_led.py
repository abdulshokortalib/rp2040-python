# =========================================================
# Nama Fail   : test_grove_led.py
# Fungsi      : Menguji Grove LED melalui pelbagai mod - hidup/mati,
#               berkelip perlahan, berkelip cepat, corak isyarat,
#               dan kawalan kecerahan (PWM fade).
# Papan       : Maker Pi RP2040
# Bahasa      : CircuitPython
# Komponen    : Grove LED (disambungkan ke port Grove)
# Pin Diguna  : LED: GP5 (Grove port 3 - pin data)
# Tahap       : Asas
# Nota        : Ujian dijalankan secara berurutan dalam satu kitaran
#               tanpa henti. Setiap ujian diulang sebelum meneruskan
#               ke ujian seterusnya.
# =========================================================

import board
import digitalio
import pwmio
import time

# ----------------------------------------------------------
# Persediaan pin LED
# GP5 ialah pin data pada port Grove 3 (Maker Pi RP2040)
# ----------------------------------------------------------
GROVE_LED_PIN = board.GP5

# ----------------------------------------------------------
# Fungsi pembantu
# ----------------------------------------------------------

def hidup_padam_biasa(led, ulangan=3, tempoh=1.0):
    """Ujian asas: hidup dan padam LED dengan selang tetap."""
    print("  [Ujian 1] Hidup/Padam biasa ({} kali, {}s)".format(ulangan, tempoh))
    for i in range(ulangan):
        led.value = True
        time.sleep(tempoh)
        led.value = False
        time.sleep(tempoh)

def berkelip_perlahan(led, ulangan=3):
    """Ujian berkelip pada kadar perlahan (0.5s setiap fasa)."""
    print("  [Ujian 2] Berkelip perlahan ({} kali, 0.5s)".format(ulangan))
    for _ in range(ulangan):
        led.value = True
        time.sleep(0.5)
        led.value = False
        time.sleep(0.5)

def berkelip_cepat(led, ulangan=10):
    """Ujian berkelip pada kadar cepat (0.1s setiap fasa)."""
    print("  [Ujian 3] Berkelip cepat ({} kali, 0.1s)".format(ulangan))
    for _ in range(ulangan):
        led.value = True
        time.sleep(0.1)
        led.value = False
        time.sleep(0.1)

def corak_sos(led):
    """Ujian corak isyarat SOS dalam kod Morse (... --- ...)."""
    print("  [Ujian 4] Corak SOS (Kod Morse)")
    TITIK = 0.15   # tempoh titik (.)
    GARISAN = 0.45  # tempoh garisan (-)
    JEDA = 0.15    # jeda antara simbol
    JEDA_HURUF = 0.45  # jeda antara huruf

    def titik():
        led.value = True
        time.sleep(TITIK)
        led.value = False
        time.sleep(JEDA)

    def garisan():
        led.value = True
        time.sleep(GARISAN)
        led.value = False
        time.sleep(JEDA)

    # S = . . .
    for _ in range(3):
        titik()
    time.sleep(JEDA_HURUF)

    # O = - - -
    for _ in range(3):
        garisan()
    time.sleep(JEDA_HURUF)

    # S = . . .
    for _ in range(3):
        titik()
    time.sleep(0.8)  # jeda akhir sebelum ulang

def fade_pwm(pin, langkah=50, tempoh_langkah=0.01):
    """
    Ujian kecerahan beransur (fade in dan fade out) menggunakan PWM.
    Mencipta objek PWM sementara kerana pin perlu dilepaskan selepas ujian.
    """
    print("  [Ujian 5] Fade in / Fade out (PWM, {} langkah)".format(langkah))
    pwm = pwmio.PWMOut(pin, frequency=1000, duty_cycle=0)
    try:
        # Fade in: gelap ke terang
        for i in range(langkah + 1):
            pwm.duty_cycle = int((i / langkah) * 65535)
            time.sleep(tempoh_langkah)
        time.sleep(0.3)
        # Fade out: terang ke gelap
        for i in range(langkah, -1, -1):
            pwm.duty_cycle = int((i / langkah) * 65535)
            time.sleep(tempoh_langkah)
        time.sleep(0.3)
    finally:
        pwm.deinit()

# ----------------------------------------------------------
# Kitaran ujian utama
# ----------------------------------------------------------
print("========================================")
print("  Ujian Grove LED - Maker Pi RP2040")
print("  Pin: GP5 (Grove Port 3)")
print("========================================")

kitaran = 0

while True:
    kitaran += 1
    print("\n--- Kitaran Ujian #{} ---".format(kitaran))

    # Ujian 1, 2, 3, 4 menggunakan digital output
    led = digitalio.DigitalInOut(GROVE_LED_PIN)
    led.direction = digitalio.Direction.OUTPUT
    led.value = False

    hidup_padam_biasa(led, ulangan=3, tempoh=1.0)
    time.sleep(0.5)

    berkelip_perlahan(led, ulangan=4)
    time.sleep(0.5)

    berkelip_cepat(led, ulangan=10)
    time.sleep(0.5)

    corak_sos(led)
    time.sleep(0.5)

    # Lepaskan pin digital sebelum guna PWM
    led.deinit()

    # Ujian 5 menggunakan PWM pada pin yang sama
    fade_pwm(GROVE_LED_PIN, langkah=50, tempoh_langkah=0.01)
    time.sleep(0.5)

    print("--- Semua ujian selesai. Berehat 2 saat... ---")
    time.sleep(2.0)
