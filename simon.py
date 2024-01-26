import board
import digitalio as dio
import time
import random

#LEDs and Buttons
button_w = dio.DigitalInOut(board.D8)
button_w.direction = dio.Direction.INPUT
led_w = dio.DigitalInOut(board.D9)
led_w.direction = dio.Direction.OUTPUT


button_g = dio.DigitalInOut(board.D6)
button_g.direction = dio.Direction.INPUT
led_g = dio.DigitalInOut(board.D7)
led_g.direction = dio.Direction.OUTPUT

button_y = dio.DigitalInOut(board.D4)
button_y.direction = dio.Direction.INPUT
led_y = dio.DigitalInOut(board.D5)
led_y.direction = dio.Direction.OUTPUT

button_r = dio.DigitalInOut(board.D2)
button_r.direction = dio.Direction.INPUT
led_r = dio.DigitalInOut(board.D3)
led_r.direction = dio.Direction.OUTPUT

on_off = dio.DigitalInOut(board.D10)
on_off.direction = dio.Direction.INPUT

"""
This code outputs the sequence that the user needs to match.
# red led = 1 point all leds = 10 points
"""
def sequence(light_speed):
    for x in list1:
        if x == 0:
            led_w.value = True
            time.sleep(light_speed)
            led_w.value = False
        if x == 1:
            led_g.value = True
            time.sleep(light_speed)
            led_g.value = False
        if x == 2:
            led_y.value = True
            time.sleep(light_speed)
            led_y.value = False
        if x == 3:
            led_r.value = True
            time.sleep(light_speed)
            led_r.value = False
        if on_off.value == False:
            off = True
        time.sleep(light_speed/2)
        
#adds to the point count 
def add(points):
    list1.append(random.choice(colors))
    points += 1
    return points

#Checks the user's inputs and returns whether it matches the sequence displayed.
def check(speed):
    for i in list1:
        color = None
        while color == None:
            if button_w.value == True:
                led_w.value = True
                time.sleep(0.3)
                led_w.value = False
                color = 0
            if button_g.value == True:
                led_g.value = True
                time.sleep(0.3)
                led_g.value = False
                color = 1
            if button_y.value == True:
                led_y.value = True
                time.sleep(0.3)
                led_y.value = False
                color = 2
            if button_r.value == True:
                led_r.value = True
                time.sleep(0.3)
                led_r.value = False
                color = 3
            if on_off.value == True:
                off = True
                return False
        time.sleep(0.1)
        if color != i:
            return False
    return True
    
#displays points using green leds for a single point and blinking all leds for 10 points        
def endgame(points, speed):
    print(int(points/10))
    for i in range(int(points / 10)):
        led_w.value = True
        led_g.value = True
        led_y.value = True
        led_r.value = True
        time.sleep(speed)
        led_w.value = False
        led_g.value = False
        led_y.value = False
        led_r.value = False
        time.sleep(speed)
    for i in range((points % 10)):
        led_g.value = True
        time.sleep(speed)
        led_g.value = False
        time.sleep(speed)
            
#0 = white  1 = green  2 = yellow  3 = red
colors = (0,1,2,3)
light_speed = 1
check_speed = 0.3


while True:
    off = False
    list1 = [random.choice(colors)]
    points = 0
    if on_off.value:
        #turning on lights to show game is starting
        game = True
        for i in range(3):
                led_w.value = True
                led_g.value = True
                led_y.value = True
                led_r.value = True
                time.sleep(light_speed)
                led_w.value = False
                led_g.value = False
                led_y.value = False
                led_r.value = False
                time.sleep(light_speed)
        while game:
            #prints sequence 
            sequence(light_speed)
            #checks if off button was pressed
            if off == True or on_off.value == True:
                game = False
            #if of button wasn't pressed it runs the user's button input.
            else:
                game = check(check_speed)
            if game:
                points = add(points)
            #When game is wrong print out code but if it was turn off with off button reset game and don't print out any points.
            elif off and not game:
                endgame(points, light_speed)
