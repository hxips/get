import RPi.GPIO as gpio
import time
def decimal2binary(value): 
    return [int(bit) for bit in bin(value)[2:].zfill(8)]
def analogVoltage(num):
    global dacPins
    for i,val in enumerate(decimal2binary(num)):
                    gpio.output(dacPins[i],val)
def adc()->float:
    global dacPins,compPin
    left,right =0,255
    for _ in range(8):
        volt = left + (right-left)//2
        analogVoltage(volt)
        time.sleep(0.07)
        if not gpio.input(compPin):
            right = volt
        else:
            left = volt
    print(3.3*(left + (right-left)//2)/255)
    return    3.3*(left + (right-left)//2)/255   
            

  

gpio.setmode(gpio.BCM)
dacPins = [26,19,13,6,5,11,9,10]
gpio.setup(dacPins,gpio.OUT,initial = 0)
ledPins = [24,25,8,7,12,16,20,21]
compPin = 4
gpio.setup(compPin,gpio.IN)
potVoltage = 17
gpio.setup(potVoltage,gpio.OUT,initial = 1)
maxVoltage = 3.3
gpio.setup(ledPins,gpio.OUT)
try:
    while True:
        alpha = int(adc()/maxVoltage*9)

        leds = [0]*(8-alpha)+[1]*alpha
        for i,val in enumerate(ledPins):
            gpio.output(val,leds[i])


finally:
    gpio.output(dacPins,0)
    gpio.cleanup()
