import RPi.GPIO as GPIO
import time

def bining(val: int) -> list:
    return [int(bit) for bit in format(val, 'b').zfill(8)]

def volt(num, dacP: list):
    for i, j in enumerate(bining(num)):
        GPIO.output(dacP[i], j)

def adc(dacP: list, compP: int, left=0, right=255) -> float:
    for _ in range(8):
        v = left + (right - left) // 2
        volt(v, dacP)
        if not GPIO.input(compP):
            right = v
        else:
            left = v
        v = left + (right - left) // 2
    # print('---%s seconds ---' % (time.time() - start_time))
    time.sleep(0.05)
    return 3.3*v / 255

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
