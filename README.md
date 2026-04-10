# rp2040-python

Repositori ini menghimpunkan koleksi contoh kod **CircuitPython** untuk papan **Maker Pi RP2040**.  
Kandungan repo ini sesuai untuk pembelajaran kendiri, demonstrasi pengajaran TVET, dan ujian asas komponen elektronik seperti LED, buzzer, LCD, motor, butang, dan sensor ultrasonik.

## Objektif Repositori

Repo ini dibangunkan untuk membantu pengguna:

- memahami asas penggunaan Maker Pi RP2040
- mempelajari kawalan input dan output menggunakan CircuitPython
- menguji komponen secara langkah demi langkah
- membina projek mini berasaskan sensor dan aktuator
- menggunakan contoh kod sedia ada sebagai asas untuk projek sendiri

## Platform dan Keperluan Asas

Sebelum menggunakan fail dalam repo ini, pastikan perkara berikut tersedia:

- papan **Maker Pi RP2040**
- firmware **CircuitPython**
- editor seperti **Thonny**
- sambungan komponen yang betul
- library tambahan bagi fail tertentu seperti:
  - `adafruit_motor`
  - `neopixel`
  - `neopixel_write`

## Struktur Kandungan Repo

Kandungan repo ini boleh dibahagikan kepada beberapa kumpulan utama:

### 1. LED Asas
Fail:
- `led1.py`
- `led2.py`
- `led3.py`
- `led4.py`
- `led5.py`
- `groveled1.py`

Topik:
- LED hidup dan padam
- dua LED serentak
- dua LED berselang-seli
- kawalan LED menggunakan butang
- toggle LED
- penggunaan Grove LED

### 2. Buzzer dan Audio
Fail:
- `beep.py`
- `beep_loop.py`
- `buzzer2.py`
- `buzzer3.py`
- `buzzer_continue.py`
- `grovebuzzer3.py`
- `siren.py`
- `happy_birthday.py`
- `doraemon.py`
- `lagu_button.py`

Topik:
- buzzer sekali bunyi
- buzzer berulang
- bunyi siren
- melodi asas
- pemain lagu menggunakan butang

### 3. Motor DC
Fail:
- `motor1.py`
- `motor2.py`
- `motor3.py`
- `motor4.py`
- `motor5.py`

Topik:
- gerakan motor ke hadapan
- forward dan reverse
- kawalan kelajuan
- butang sebagai kawalan motor
- toggle motor on/off

### 4. LCD dan Paparan
Fail:
- `test_lcd.py`
- `lcd_button.py`
- `ambulan.py`
- `av_car.py`
- `us2.py`
- `us4.py`

Topik:
- ujian paparan LCD I2C
- paparan mesej sistem
- integrasi LCD dengan butang, sensor, atau motor

### 5. Ultrasonik
Fail:
- `us2.py`
- `us3.py`
- `us4.py`
- `av_car.py`

Topik:
- bacaan jarak
- paparan jarak pada LCD
- kawalan motor berdasarkan jarak
- asas logik kereta autonomi

### 6. Projek Mini
Fail:
- `ambulan.py`
- `ambulan_motor.py`
- `av_car.py`
- `code.py`

Topik:
- sistem amaran
- siren dan LED kecemasan
- simulasi motor dan amaran
- prototaip kereta autonomi ringkas
- demo asal papan Maker Pi RP2040

## Jadual Ringkas Pin

> **Nota penting:** sesetengah fail menggunakan pin yang berbeza walaupun fungsi hampir sama. Semak kod sebelum sambungan dibuat.

| Fail | Fungsi | Pin Utama |
|---|---|---|
| `led1.py` | LED blink | GP0 |
| `led2.py` | 2 LED serentak | GP0, GP1 |
| `led3.py` | 2 LED berselang-seli | GP0, GP1 |
| `led4.py` | Button kawal LED | GP0, GP20 |
| `led5.py` | Toggle LED | GP0, GP20 |
| `groveled1.py` | Grove LED | GP5 |
| `beep.py` | Beep sekali | GP22 |
| `beep_loop.py` | Beep 3 kali | GP22 |
| `buzzer2.py` | Buzzer + LED | GP22, GP0 |
| `buzzer3.py` | Melodi ringkas | GP22 |
| `buzzer_continue.py` | Buzzer berterusan | GP22 |
| `grovebuzzer3.py` | Grove buzzer + LED | GP17, GP5 |
| `siren.py` | Siren | GP22 |
| `happy_birthday.py` | Lagu Happy Birthday | GP22 |
| `doraemon.py` | Lagu Doraemon + NeoPixel | GP22, GP18 |
| `lagu_button.py` | Pemilih lagu | GP20, GP21, GP22, GP18 |
| `motor1.py` | Motor forward | GP8, GP9 |
| `motor2.py` | Motor forward/reverse | GP8, GP9 |
| `motor3.py` | Motor ramp speed | GP8, GP9 |
| `motor4.py` | Button kawal motor | GP8, GP9, GP20 |
| `motor5.py` | Toggle motor | GP8, GP9, GP20 |
| `test_lcd.py` | LCD I2C test | GP3=SCL, GP2=SDA |
| `lcd_button.py` | LCD + buzzer + button + LED | GP3, GP2, GP22, GP20, GP18 |
| `us2.py` | Ultrasonic + LCD | GP1, GP3, GP2 |
| `us3.py` | Ultrasonic + motor | GP1, GP8, GP9 |
| `us4.py` | Ultrasonic + LCD + motor | GP1, GP3, GP2, GP8, GP9 |
| `ambulan.py` | LCD + buzzer + button + LED | GP3, GP2, GP22, GP20, GP5 |
| `ambulan_motor.py` | LCD + buzzer + 2 butang + LED + motor | GP1, GP0, GP22, GP20, GP21, GP5, GP8, GP9 |
| `av_car.py` | Motor + ultrasonic + LCD | GP8, GP9, GP1, GP3, GP2 |

## Fail Yang Perlu Diperhatikan

Beberapa fail dalam repo ini masih memerlukan penjelasan atau penamaan semula supaya lebih jelas:

- `buzzer1.py` kini lebih menyerupai contoh LED, bukan buzzer
- `us1.py` kini lebih menyerupai contoh LED blink, bukan ultrasonic
- `ambulan_motor.py` menggunakan konfigurasi LCD yang berbeza daripada fail LCD lain

Disyorkan supaya fail-fail ini sama ada:
- dikemas kini kandungannya supaya sepadan dengan nama fail, atau
- dinamakan semula supaya sepadan dengan fungsi sebenar

## Cadangan Urutan Pembelajaran

Untuk pengguna baharu, urutan ini lebih sesuai:

1. `led1.py`
2. `led2.py`
3. `led3.py`
4. `led4.py`
5. `led5.py`
6. `beep.py`
7. `beep_loop.py`
8. `buzzer3.py`
9. `test_lcd.py`
10. `motor1.py`
11. `motor2.py`
12. `motor3.py`
13. `us2.py`
14. `us3.py`
15. `us4.py`
16. `ambulan.py`
17. `av_car.py`

## Cara Guna

1. Pasang CircuitPython pada papan Maker Pi RP2040.
2. Sambungkan papan ke komputer.
3. Buka fail yang ingin diuji menggunakan Thonny.
4. Semak pin dan komponen yang digunakan.
5. Simpan fail ke papan sebagai `code.py` jika mahu ia berjalan automatik.
6. Uji fungsi dan perhatikan tindak balas komponen.

## Cadangan Penambahbaikan Repo

Untuk menjadikan repo ini lebih mantap dan mesra pengguna, cadangan berikut sangat digalakkan:

- tambah komen header standard pada semua fail
- tambah gambar sambungan litar
- asingkan fail mengikut folder seperti `led/`, `buzzer/`, `motor/`, `lcd/`, `ultrasonic/`, `project/`
- tukar nama fail yang mengelirukan
- tambah `requirements.md` atau `libraries.md`
- tambah tahap kesukaran pada setiap fail
- tambah rajah pin Maker Pi RP2040

## Penutup

Semoga repo ini membantu pelajar, pengajar, dan pemula memahami penggunaan Maker Pi RP2040 dengan lebih mudah, tersusun, dan praktikal. Repositori ini juga boleh dijadikan asas untuk menghasilkan modul latihan TVET, eksperimen mikropengawal, dan projek mini berasaskan CircuitPython.
