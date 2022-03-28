import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

def bining(val: int) -> list:
    return [int(bit) for bit in format(val, 'b').zfill(8)]


pin = 7
GPIO.setup(pin, GPIO.OUT)

pwm = GPIO.PWM(pin, 5)
pwm.start(0)
try:
    n = input('Число от 0 до 100: ')
    while n != 'q':
        pwm.start(float(n))
        n = input()
finally:
    pwm.stop()
    GPIO.output(pin, 0)
    GPIO.cleanup()
