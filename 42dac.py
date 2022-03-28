import RPi.GPIO as GPIO
import time


def bining(val: int) -> list:
    return [int(bit) for bit in format(val, 'b').zfill(8)]


GPIO.setmode(GPIO.BCM)


period = float(input("Период = "))
dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT)
try:
    i = 0
    while True:
        bi = bining(i%256)
        for j in range(len(bi)):
            GPIO.output(dac[j], bi[j])
        time.sleep(period/512)
        i += 1
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()