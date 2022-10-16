# Hardware driver for self-excited buzzer
# MicroPython version: v1.19.1 on 2022-06-18
# Test device: Espressif ESP32-WROOM-32

class Buzzer:
	def __init__(self, pin):
		self.pin = pin
		self.pin.init()

