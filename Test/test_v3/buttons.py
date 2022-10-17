# Hardware driver for buttons
# MicroPython version: v1.19.1 on 2022-06-18
# Test device: Espressif ESP32-WROOM-32

class Buttons:
    def __init__(self, timer, **buttons):
        self.timer = timer # time.Timer
        self.buttons = buttons # {"button name": Pin object}
        
        self.handlers = {} # set by self.assign
        self.timer_period = -1 # set by self.detectperiod
        self.timer_mode = self.timer.PERIODIC # periodically check the state of buttons
        self.timer_callback = None # initially do nothing after each period
        
        self._initbuttons()
        self._settimer()

    def _initbuttons(self):
        # set pins of all buttons as pull-down and input pins
        for button_pin in self.buttons.values():
            button_pin.init(button_pin.IN, button_pin.PULL_DOWN)
    
    def _settimer(self):
        # configure the timer for detecting states of pins
        self.timer.init(
            mode=self.timer_mode,
            period=self.timer_period,
            callback=self.timer_callback)
    
    def _callback(self, arg):
        # periodically called by the timer
        # detect pin state and call corresponding handler if at high level
        for button in self.buttons:
            if self.buttons[button].value() == 1:
                self.handlers[button][0](*self.handlers[button][1])
    
    def start(self, period):
        # start the timer for checking pins
        self.timer_period = period # set the period of checking states of buttons
        self.timer_callback = self._callback
        self._settimer()
    
    def stop(self):
        # stop checking pins
        self.timer.deinit()
    
    def assign(self, button, handler, args = ()):
        # assign function or method to corresponding pin
        # button: name of button stored as a key of self.buttons
        # handler: function or method object called when this button is pushed down
        # args: arguments provided to the handler, no argument is provided if not specify
        self.handlers[button] = (handler, args)

# ============================================
from machine import Pin, Timer
from time import sleep

class Test:
    def __init__(self):
        self.a = 1
        self.b = 2
    
    def add_a(self, a, r, g):
        self.a += 1
        print("a += 1", a, r, g)
        sleep(3)
    
    def add_b(self):
        self.b+= 1
        print("b += 1")
    
    def subtract_a(self):
        self.a -= 1
        print("a -= 1")
        
    def subtract_b(self):
        self.b -= 1
        print("b -= 1")
    
    def show_a(self):
        print("a =", self.a)
    
    def show_b(self):
        print("b =", self.b)

t = Test()
b = Buttons(Timer(0),
    aplus=Pin(27),
    asub=Pin(5),
    bplus=Pin(23),
    bsub=Pin(22),
    showa=Pin(4),
    showb=Pin(2))

b.detectperiod(100)
b.assign("aplus", t.add_a, ("wow", "gee", "gao"))
b.assign("asub", t.subtract_a)
b.assign("bplus", t.add_b)
b.assign("bsub", t.subtract_b)
b.assign("showa", t.show_a)
b.assign("showb", t.show_b)
b.start()

i = 0
while True:
    sleep(0.1)
    print(i)
    i+=1