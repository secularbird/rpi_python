import machine,uos
import utime,sdcard

led_onboard = machine.Pin(25, machine.Pin.OUT)
led_onboard.value(0)     # onboard LED OFF for 0.5 sec
utime.sleep(0.5)
led_onboard.value(1)

print(machine.ADC(4).read_u16())
conversion_factor = 3.3 / (65535)

sda=machine.Pin(16)
scl=machine.Pin(17)

i2c=machine.I2C(0, sda=sda, scl=scl, freq=400000)

from ssd1306 import SSD1306_I2C
oled = SSD1306_I2C(128, 32, i2c)

oled.text('Welcome to the', 0, 0)
oled.text('Pi Pico', 0, 10)
oled.text('Display Demo', 0, 20)
oled.show()

from ili934x import ILI9341, color565

cs0 = machine.Pin(5)
sck0 = machine.Pin(2)
mosi0 = machine.Pin(3)
miso0 = machine.Pin(4)

spi = machine.SPI(0, mosi=mosi0, miso=miso0, sck=sck0)

sd = sdcard.SDCard(1, sck=10, mosi=11, miso=12, cs=13)
print(uos.listdir("/sd"))

count = 0
while True:
    reading = machine.ADC(4).read_u16() * conversion_factor
    temperature = 27.3 - (reading - 0.706)/0.001721
    oled.fill(0)
    oled.text(str(temperature),20,10)
    oled.text(str(count),20,20)  
    print(reading, temperature)
    oled.show()
    utime.sleep(1)
    count+=1

