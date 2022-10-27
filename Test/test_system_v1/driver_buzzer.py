# MicroPython version: v1.19.1 on 2022-06-18
# Espressif ESP32-WROOM-32

class Buzzer:
    def __init__(self, pin, timer):
        self.pin = pin # the machine.Pin object connected to the buzzer module
        self.timer = timer # machine.Timer object used to turn the buzzer off
        self._init()


    def _init(self):
        self.mute = False # initially turn off the mute mode
        self.pin.init(mode=self.pin.OUT) # set the pin as an OUT pin
        self.off() # initially turn off the buzzer


    def _settimer(self, period):
        # initialize the timer for turning off the buzzer after a certain period of time 
        self.timer.init(mode=self.timer.ONE_SHOT, period=period, callback=self.off)


    def on(self):
        # activate the mosfit controlling the buzzer
        if not self.mute:
            self.pin.off()


    def off(self, _=None):
        # inactivate the mosfit controlling the buzzer
        self.pin.on()


    def buzz(self, duration):
        # buzz for a certain duration
        # duration (ms)
        if not self.mute:
            self.pin.off()
            self._settimer(duration)
