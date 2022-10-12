# Hardware driver of discrete LED matrices with max7219
# MicroPython version: v1.19.1 on 2022-06-18
# Test device: Espressif ESP32-WROOM-32

from micropython import const

# declare register addresses as constants
NOOP = const(0x0)
DIGIT0 = const(0x1)
DIGIT1 = const(0x2)
DIGIT2 = const(0x3)
DIGIT3 = const(0x4)
DIGIT4 = const(0x5)
DIGIT5 = const(0x6)
DIGIT6 = const(0x7)
DIGIT7 = const(0x8)
DECODEMODE = const(0x9)
INTENSITY = const(0xA)
SCANLIMIT = const(0xB)
SHUTDOWN = const(0xC)
DISPLAYTEST = const(0xF)

class DiscreteMax7219Matrices:
    def __init__(self, spi, cs_pins):
        # spi (machine.SPI): serial phripheral interface
        # cs_pins (tuple): elements of the tuple are instances of machine.Pin
        self.spi = spi
        self.cs_pins = cs_pins
        self._init()
    
    def _init(self):
        self.spi.init(baudrate=9000000, polarity=0, phase=0, firstbit=self.spi.MSB)
        for cs_pin in self.cs_pins:
            cs_pin.init(mode=Pin.OUT, drive=Pin.DRIVE_0)
        self.switch(1)
        self.test(0)
        self.intensity(6)
        self._writeall(SCANLIMIT, 0x7)
        self._writeall(DECODEMODE, 0x0)
        for i in range(8):
            self._writeall(DIGIT0+i, 0b00000000)

    def _writeall(self, addr, data):
        # write same data into each max7219
        for cs_pin in self.cs_pins:
            cs_pin.off()
        self.spi.write(bytearray([addr, data]))
        for cs_pin in self.cs_pins:
            cs_pin.on()
    
    def writerow(self, cs_index, row_index, data):
        # write the data of a specific row to a specific chip
        self.cs_pins[cs_index].off()
        self.spi.write(bytearray([DIGIT0+row_index, data]))
        self.cs_pins[cs_index].on()
    
    def clear(self):
        # turn off every LED
        for i in range(8):
            self._writeall(DIGIT0+i, 0b00000000)
    
    def test(self, on):
        if on == 1:
            self._writeall(DISPLAYTEST, 0x1)
        elif on == 0:
            self._writeall(DISPLAYTEST, 0x0)

    def intensity(self, i):
        if 0 <= i <= 15:
            self._writeall(INTENSITY, i)
    
    def switch(self, state):
        # turn on \ off the power supply to each LED
        if state == 1:
            # switch on
            self._writeall(SHUTDOWN, 0x1)
        elif state == 0:
            # switch off
            self._writeall(SHUTDOWN, 0x0)