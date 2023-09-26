import time
import board
import neopixel
import random
from adafruit_led_animation.animation.solid import Solid
from adafruit_led_animation.animation.blink import Blink
from adafruit_led_animation.animation.colorcycle import ColorCycle
from adafruit_led_animation.animation.chase import Chase
from adafruit_led_animation.animation.comet import Comet
from adafruit_led_animation.animation.pulse import Pulse
from adafruit_led_animation.sequence import AnimationSequence
from adafruit_led_animation.color import RED,YELLOW,ORANGE,GREEN,TEAL,CYAN,BLUE,PURPLE,MAGENTA,WHITE,BLACK,GOLD,PINK,AQUA,JADE,AMBER,OLD_LACE
np = neopixel.NeoPixel(board.D2, 30, auto_write = False, brightness = 0.2)

colors = [[0,0,255],[255,0,0],[255,255,255]]
speed = 0.01
times = 50
i = 0
color = [0,0,255]
fOrange1 = (255,54,0)
fOrange2 = (255,74,0)
fOrange3 = (255,34,0)
red = (255,0,0)
black = (0,0,0)
purple = (50,0,50)
fColors = [fOrange1,fOrange2,fOrange3,red,black]
lightningColor = [[255,255,255],[0,255,0]]
pixel_num = 30
pixel_pin = board.D2
'''

Function: fadeOut

Description: It fades out a specified color by lower the RGB value till it goes to 0.

Parameters: color-list, speed-int

Return value: "none"

'''
def fadeOut(color = [0,0,255], speed=1):
    if speed <= 0:
        speed = 1
    fadeR = color[0]/256.0
    fadeG = color[1]/256.0
    fadeB = color[2]/256.0
    color1 = [color[0],color[1],color[2]]
    np.fill(color1)
    np.show()
    for i in range(255):
        color1[0] = int (color[0] - (fadeR*i))
        color1[1] = int (color[1] - (fadeG*i))
        color1[2] = int (color[2] - (fadeB*i))
        np.fill(color1)
        np.show()
        print(color1)
        time.sleep(speed)
'''

Function: fadeIn

Description: It fades in a specified color by increasing the RGB value from black till it goes to the specified color.

Parameters: color-list, speed-int

Return value: "none".

'''
def fadeIn(color = [0,0,255], speed=1):
    if speed <= 0:
        speed = 1
    fadeR = color[0]/256.0
    fadeG = color[1]/256.0
    fadeB = color[2]/256.0
    color1 = [0,0,0]
    np.fill(color1)
    np.show()
    print(color1)
    for i in range(255):
        color1[0] = int (fadeR*i)
        color1[1] = int (fadeG*i)
        color1[2] = int (fadeB*i)
        np.fill(color1)
        np.show()
        time.sleep(speed)
        print(color1)
'''

Function: chase

Description: It creates a chasing effect by incrementing the spacing of the leds over time making a chase illusion.

Parameters: times-int, color-list, color2-list, speed-float

Return value: "none".

'''
def chase(times = 1, color = [0,0,0],color2 = [255,255,255], speed = 0.1):
    for j in range(times):
        np.show()
        for i in range(30):
            if i % 3 != 0:
                led = (i+j) % 30 
                np[led] = color2
                print("bColor",i,np[i])
            elif i % 3 == 0:
                led = (i+j) % 30
                np[led] = color
                print("fColor",i,np[i])
            time.sleep(speed)
'''

Function: sparkle

Description: It sets a random led to color2 while the backrgound is set to color then sets all of the leds back to color and sets random leds to color2 again. 

Parameters: color-list, color2-list, times-int

Return value: "none".

'''
def sparkle(color = [0,0,255],color2 = [255,255,255], tim = 1):
    for i in range(tim):
        np.fill(color)
        led1 = random.randint(0, 28)
        led2 = random.randint(0, 28)
        led3 = random.randint(0, 28)
        np[led1] = color2
        np[led2] = color2
        np[led3] = color2
        np.show()
        print("sparkle")
        time.sleep(0.1)

def fire(colors, speed = 0.1):
    led = [random.randint(0,29) for i in range(30)]
    for i in led:
        delay = random.random()/2
        np[i] = colors[random.randint(0,4)]
        time.sleep(delay)
        np.show()
        print("fire",delay)
def lightning(color,lColors, speed = 0.1):
    delay = random.random()*5 + 0.5
    np.fill(color)
    np.show()
    time.sleep(delay)
    ind = random.randint(0, len(lColors)-1)
    for i in range(random.randint(1,4)):
        np.fill(lColors[ind])
        np.show()
        time.sleep(0.1)
        np.fill([0,0,0])
        np.show()
    np.fill(color)
    np.show()
solid = Solid(np, color=PINK)
blink = Blink(np, speed=0.5, color=OLD_LACE)
colorcycle = ColorCycle(np, 0.5, colors=[MAGENTA, ORANGE, TEAL])
chase = Chase(np, speed=0.5, color=JADE, size=3, spacing=3)
comet = Comet(np, speed=0.1, color=PURPLE, tail_length=10, bounce=True)
pulse = Pulse(np, speed=0.5, color=AMBER, period=3)
animations = AnimationSequence(
    comet, blink, chase, solid, pulse, colorcycle, advance_interval=5, auto_clear=True, random_order=True)
#This while true makes a lightshow based on an American theme of red white and blue.
#np.fill(red)
while True:
    animations.animate()
'''
    lightning(purple,lightningColor)
    fadeOut(color, speed)
    fadeIn(colors[i], speed)
    sparkle(colors[i], colors[(i+1)%3], times)
    chase(times, colors[(i-1)%3], colors[i], speed)
    color = colors[i]
    i = (i + 1) % 3
'''

