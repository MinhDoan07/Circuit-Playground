import time
import board
import neopixel
import random
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)
while True:
    i = random.randint(0, 9)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    pixels[i] = ((r, g, b))