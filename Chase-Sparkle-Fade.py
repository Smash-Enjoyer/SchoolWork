import time
import board
import neopixel
import random
np = neopixel.NeoPixel(board.D2, 30, auto_write = True, brightness = 1)

color = [255,156,127]
speed = 3
times = 1
def fadeOut(color, speed=1):
    if speed <= 0:
        speed = 1
    fadeR = color[0]/256.0
    fadeG = color[1]/256.0
    fadeB = color[2]/256.0
    color1 = [color[0],color[1],color[2]]
    np.fill(color1)
    for i in range(255):
        color1[0] = int (color[0] - (fadeR*i))
        color1[1] = int (color[1] - (fadeG*i))
        color1[2] = int (color[2] - (fadeB*i))
        np.fill(color1)
        print(color1)
        time.sleep(1.0/(10*speed))
def fadeIn(color, speed=1):
    if speed <= 0:
        speed = 1
    fadeR = color[0]/256.0
    fadeG = color[1]/256.0
    fadeB = color[2]/256.0
    color1 = [0,0,0]
    np.fill(color1)
    print(color1)
    for i in range(255):
        color1[0] = int (fadeR*i)
        color1[1] = int (fadeG*i)
        color1[2] = int (fadeB*i)
        np.fill(color1)
        time.sleep(1.0/(10*speed))
        print(color1)
def chase(color = [0,0,0], speed = 1):
    for j in range(30):
        for i in range(0,30, 3):
            led = (i+j)%29
            np[led] = color
            np[led - 1] = [0,0,0]
            np[led - 2] = [0,0,0]
            time.sleep(1/(10*speed))
def sparkle(color = [0,0,0], speed = 1, times = 1):
    for i in range(times):
        np.fill(color)
        led1 = random.randint(0, 28)
        led2 = random.randint(0, 28)
        led3 = random.randint(0, 28)
        np[led1] = [12,124,42]
        np[led2] = [12,124,42]
        np[led3] = [12,124,42]
        time.sleep(1/(10*speed))

while True:
    fadeIn(color, speed)
    fadeOut(color, speed)
    sparkle(color, speed, 10)
    chase(color, speed)
