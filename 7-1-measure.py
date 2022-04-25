import RPi.GPIO as gpio
import matplotlib.pyplot as plt
import time


def dec2bin(num):
    return [int(bit) for bit in bin(num)[2:].zfill(8)]


def num2dac(num):
    signal = dec2bin(num)
    gpio.output(dac, signal)
    return signal


def getnum(arr):
    num = 0
    for i, elem in enumerate(arr):
        num += elem * (2 ** (7 - i))
    return num


def adc():
    arr = [0] * 8
    num = 0
    for i in range(8):
        arr[i] = 1
        num = getnum(arr)
        if i == 8:
            return None
        num2dac(num)
        time.sleep(0.01)
        comp_value = gpio.input(comp)

        if comp_value == 0:
            arr[i] = 0
    return num


gpio.setmode(gpio.BCM)
data = []
leds = [21, 20, 16, 12, 7, 8, 25, 24]
gpio.setup(leds, gpio.OUT)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
gpio.setup(dac, gpio.OUT)
comp = 4
gpio.setup(comp, gpio.IN)
troy = 17
gpio.setup(troy, gpio.OUT, initial=1)
start = time.time()

try:
    while True:
        gpio.output(troy, 1)
        current = adc()
        time.sleep(1)
        gpio.output(leds, dec2bin(current))
        num = current / 256 * 3.3
        print(num)
        data.append(num)
        if num > 2.5:
            break
    
    gpio.output(troy, 0)
    while True:
        current = adc()
        time.sleep(0.01)
        gpio.output(leds, dec2bin(current))
        num = current / 256 * 3.3
        data.append(num)
        if num < 0.5:
            break
    
    end = time.time()
    print("Время :", end - start, "\nЧастота :", 1, "\nШаг :", 8)
    plt.plot(data)
    plt.show()

    data = list(map(str, data))
    with open("data.txt", 'w') as file:
        file.write("\n".join(data))

finally:
    gpio.output(leds, 0)
    gpio.output(troy, 0)
    gpio.cleanup()