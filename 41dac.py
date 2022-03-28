import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

def bining(val: int) -> list:
    return [int(bit) for bit in format(val, 'b').zfill(8)]


dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT)
try:
    n = input()
    while n != 'q':
        if not n.isnumeric():
            print('Не числовое значение')
        else:
            if not n.isdigit():
                print('Не целое')
            else:
                n = int(n)
                if n<0 or 255<n:
                    print('Неподерживаемое значение')
                else:
                    bi = bining(n)
                    for i in range(len(bi)):
                        GPIO.output(dac[i], bi[i])
        n = input()
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()