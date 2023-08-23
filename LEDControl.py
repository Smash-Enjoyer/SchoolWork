#imports
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

led1.value = True
#Code to turn on the lights
def on():
   
   led1.value = not btn_on.value
   time.sleep(0.01)
   led2.value = not btn_on.value
   time.sleep(0.01)
   led3.value = not btn_on.value
   time.sleep(0.01)
   led4.value = not btn_on.value
   time.sleep(0.01)


#Code to turn off the light
def off():
   led1.value = btn_off.value
   time.sleep(0.01)
   led2.value = btn_off.value
   time.sleep(0.01)
   led3.value = btn_off.value
   time.sleep(0.01)
   led4.value = btn_off.value
   time.sleep(0.01)    
   
    
#Code to dim the lights
def dim():
    for i in range(20):
        on = i
        off = 100 - on
        for j in range(1):
            led.value = True
            time.sleep(on / 10000.0)
            led.value = False
            time.sleep(off / 10000.0)
	print(on)
#Code to brighten the lights
def brighten():
    for i in range(20):
        on = 100-i-1
        off = 100 - on
        for j in range(1):
            led.value = True
            time.sleep(on / 10000.0)
            led.value = False
            time.sleep(off / 10000.0)
    print(on)



while True: 
    if btn_off.value == True:
        off()
    else:
        on()
	if btn_dim.value == False:
		dim()
	else if btn_bright.vlaue == False:
		brighten()
