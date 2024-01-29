
from adafruit_circuitplayground import cp
wav = "MEOW.wav"
while True:
    if cp.button_a:
        cp.play_file(wav)
    if cp.button_b:
        cp.play_file(wav)

