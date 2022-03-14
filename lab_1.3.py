import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.IN)


while __main__ == __name__:
    GPIO.output(17, GPIO.input(27))
