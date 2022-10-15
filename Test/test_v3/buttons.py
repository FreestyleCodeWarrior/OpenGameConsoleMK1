# Hardware driver of buttons for man-machine interaction
# MicroPython version: v1.19.1 on 2022-06-18
# Test device: Espressif ESP32-WROOM-32

class Buttons:
    def __init__(self, pin, **btn):
        self.pin = pin
        self.btn = btn
        self._init()

    def _init(self):
        for b in self.btn.values():
            b.init(self.pin.IN, self.pin.PULL_DOWN)

    def get(self, name):
        return self.btn[name].value()

from machine import Pin
from time import sleep

def hdr(arg):
    for i in range(5):
        print(i, arg, type(arg))
        sleep(0.5)

Pin.irq(Pin(2, Pin.IN, Pin.PULL_DOWN), handler=hdr, trigger=Pin.IRQ_RISING)
Pin.irq(Pin(4, Pin.IN, Pin.PULL_DOWN), handler=hdr, trigger=Pin.IRQ_RISING)
Pin.irq(Pin(5, Pin.IN, Pin.PULL_DOWN), handler=hdr, trigger=Pin.IRQ_RISING)
Pin.irq(Pin(22, Pin.IN, Pin.PULL_DOWN), handler=hdr, trigger=Pin.IRQ_RISING)
Pin.irq(Pin(23, Pin.IN, Pin.PULL_DOWN), handler=hdr, trigger=Pin.IRQ_RISING)
Pin.irq(Pin(27, Pin.IN, Pin.PULL_DOWN), handler=hdr, trigger=Pin.IRQ_RISING)

i = 0
while True:
    print("main", i)
    i += 1
    sleep(0.5)

"""
b = Buttons(
    Pin,
    up=Pin(34),
    down=Pin(35),
    left=Pin(23),
    right=Pin(22),
    ok=Pin(4),
    back=Pin(2))

while True:
    if b.get("up"):
        print("up")
    elif b.get("down"):
        print("down")
    elif b.get("left"):
        print("left")
    elif b.get("right"):
        print("right")
    elif b.get("ok"):
        print("ok")
    elif b.get("back"):
        print("back")
    sleep(0.1)
"""