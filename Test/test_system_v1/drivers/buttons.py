# Hardware driver for buttons
# MicroPython version: v1.19.1 on 2022-06-18
# Espressif ESP32-WROOM-32

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
        for button, handler in self.handlers.items():
            if self.buttons[button].value() == 1:
                handler[0](*handler[1])
            
    
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