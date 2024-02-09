import time
import board
import neopixel
import random
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)
i = int(input("Which LED would you like to turn on? : "))
while i > 9 or i < 0:
    i = int(input("Please input a valid number"))
pixels[i] = ((0, 255, 0))
print("Now, I shall try to guess which LED you have turned on")
for x in range(5):
    guess = random.randint(0, 9)
    if guess == i:
        pixels[guess] = ((0, 0, 255))
        print("I guessed", guess, ". I was right!")
        break
    if guess != i:
        pixels[guess] = ((255, 0, 0))
        print("I guessed", guess, ". I was wrong. Let me try again.")
        time.sleep(0.5)
    
    
    
