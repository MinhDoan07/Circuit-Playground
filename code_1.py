import time
import board
import neopixel
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)
i = 0
pixels.fill((100, 100, 100))
while True:
    pixels[i] = ((100, 30, 20))
    pixels[i - 1] = ((100, 100, 100))
    i = i + 1
    time.sleep(0.05)
    if i == 10 :
        i = 0
        pixels[9] = ((0, 0, 0))
