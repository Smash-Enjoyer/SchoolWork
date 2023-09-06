import time
import board
import neopixel

np = neopixel.NeoPixel(board.NEOPIXEL, 1, auto_write = True, brightness = 0.2)

color = [255,0,0]
increase = 1
decrease = 0
count = 0
while True:
    np.fill(color)
    time.sleep(.03)
    if count == 255:
        decrease = (decrease + 1) % 3
        increase = (increase + 1) % 3
    else:
        color[decrease] -= 1
        color[increase] += 1
    count = (count + 1) % 256
