import RPi.GPIO as GPIO
# import time

def bining(val: int) -> list:
    return [int(bit) for bit in format(val, 'b').zfill(8)]

def Volt(num, dacP: list):
    for i, j in enumerate(bining(num)):
        GPIO.output(dacP[i], j)

def adc(dacP: list, compP: int) -> float:
    for i in range(255):
        Volt(i, dacP)
        if not GPIO.input(compP):
            # print('---%s seconds ---' % (time.time() - start_time))
            return 3.3*i / 255

GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT, initial = 0)
comp = 4
GPIO.setup(comp, GPIO.IN)
troyka = 17
GPIO.setup(troyka, GPIO.OUT, initial = 1)

try:
    while True:
        # start_time = time.time()
        print(adc(dac, comp))
        # time.sleep(1)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
