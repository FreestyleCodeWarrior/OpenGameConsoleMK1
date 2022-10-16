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