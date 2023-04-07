# Bleeding Rainbow Demo (Todbot Code)
import time
import rainbowio
import board
import neopixel

num_leds = 50
leds = neopixel.NeoPixel(board.D25, num_leds, brightness=0.4, auto_write=False, pixel_order=neopixel.RGB)
delta_hue = 256//num_leds
speed = 2  # higher numbers = faster rainbow spinning
i = 0
while True:
    for l in range(len(leds)):
        leds[l] = rainbowio.colorwheel( int(i*speed + l * delta_hue) % 255  )
        leds.show()  # only write to LEDs after updating them all
        i = (i+1) % 255
