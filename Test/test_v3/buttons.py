# Hardware driver of buttons for man-machine interaction
# MicroPython version: v1.19.1 on 2022-06-18
# Test device: Espressif ESP32-WROOM-32

class Buttons:
    def __init__(self, pin, **buttons):
        self.pin = pin # machine.Pin
        self.buttons = buttons # {"button name": Pin object}
        self._init()

    def _init(self):
        # set all pins as pull-down and input pins
        for button in self.buttons.values():
            button.init(self.pin.IN, self.pin.PULL_DOWN)
    
    def assign(self, button_name, handler):
        # set a trigger according to privided pin and handler
        # handler is a function or method being able to accept one positional argument
        Pin.irq(self.buttons[button_name], handler=handler, trigger=Pin.IRQ_RISING)

# ============================================
from machine import Pin
from time import sleep

class Test:
    def __init__(self):
        self.a = 1
        self.b = 2
    
    def add_a(self, arg):
        self.a += 1
    
    def add_b(self, arg):
        self.b+= 1
    
    def subtract_a(self, arg):
        self.a -= 1
        
    def subtract_b(self, arg):
        self.b -= 1
    
    def show_a(self, arg):
        print(self.a)
    
    def show_b(self, arg):
        print(self.b)





t = Test()
b = Buttons(
    Pin,
    up=Pin(2),
    down=Pin(4),
    left=Pin(5),
    right=Pin(22),
    ok=Pin(23),
    back=Pin(27))

b.assign("back", t.add_a)
b.assign("left", t.subtract_a)
b.assign("ok", t.add_b)
b.assign("right", t.subtract_b)
b.assign("down", t.show_a)
b.assign("up", t.show_b)
