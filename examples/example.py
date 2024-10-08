#!/usr/bin/env python3

from colorsys import hsv_to_rgb
from math import fmod
from time import sleep

import smileds

# Define the number of LEDs and led strips
num_leds = 30
num_strips = 8

# init the smi module with an initial brightness of 25%
smileds.leds_init(num_leds, 25)
smileds.leds_clear()

row = 0
t = 0.0
while True:

    # Build the LED data array
    leds = bytearray()
    for strip in range(num_strips):
        for led in range(num_leds):
            hue = fmod(t + (strip * .04), 1.0);
            r, g, b = hsv_to_rgb(hue, 1.0, 1.0)
            leds += bytearray(((int(r * 255), int(g * 255), int(b * 255))))

    # Set the buffer into to the smileds module
    smileds.leds_set(leds)

    # Shift them out to the strips
    smileds.leds_send()
    t += .01
    sleep(.05)

sleep(1)
