import board
import digitalio as dio
import time

led1 = dio.DigitalInOut(board.D2)
led1.direction = dio.Direction.OUTPUT
led1.value = True

led2 = dio.DigitalInOut(board.D3)
led2.direction = dio.Direction.OUTPUT
led2.value = True 

led3 = dio.DigitalInOut(board.D4)
led3.direction = dio.Direction.OUTPUT
led3.value = True 

led4 = dio.DigitalInOut(board.D5)
led4.direction = dio.Direction.OUTPUT
led4.value = True

btn_on = dio.DigitalInOut(board.D6)
btn_on.direction = dio.Direction.INPUT

btn_off = dio.DigitalInOut(board.D7)
btn_off.direction = dio.Direction.INPUT

btn_dim = dio.DigitalInOut(board.D8)
btn_dim.direction = dio.Direction.INPUT

btn_bright = dio.DigitalInOut(board.D9)
btn_bright.direction = dio.Direction.INPUT

led1.value = False
led2.value = False
led3.value = False
led4.value = False
stop = 0.001
on = 100
off = 100 - on
#brigthness 

def on():
    global on
    on = 100



def off():
    global on
    on = 0    
 
 
 
def dim():
    global on
    if on < 0:
        on = on - 20
    


def brighten():
    global on
    if on < 0:
        on = on + 20
        


while True:
    if btn_on.value == False:
        on()
        print(on)
        time.sleep(stop)
        print(off)
        time.sleep(stop)
    time.sleep(stop)
    if btn_off.value == False:
        off()
        print(on)
        time.sleep(stop)
        print(off)
        time.sleep(stop)
    time.sleep(stop)
    if btn_dim.value == False:
        dim()
        print(on)
        time.sleep(stop)
        print(off)
        time.sleep(stop)
    if btn_bright.value == False:
        brighten()
        print(on)
        time.sleep(stop)
        print(off)
        time.sleep(stop)
    time.sleep(stop)
    led1.value = True
    led2.value = True
    led3.value = True
    led4.value = True            
    time.sleep(on / 10000.0)
    led1.value = not True
    led2.value = not True
    led3.value = not True
    led4.value = not True
    time.sleep(off / 10000.0)

    
