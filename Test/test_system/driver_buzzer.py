from time import sleep_ms


class Buzzer:
    def __init__(self, pin):
        self.pin = pin # the machine.Pin object connected to the buzzer module
        self._init()


    def _init(self):
        self.mute = False # initially turn off the mute mode
        self.pin.init(mode=self.pin.OUT) # set the pin as an OUT pin
        self.off() # initially turn off the buzzer


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
        self.on()
        sleep_ms(duration)
        self.off()
