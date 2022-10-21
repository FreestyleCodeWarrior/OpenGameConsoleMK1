# Hardware driver of discrete LED matrices with max7219
# MicroPython version: v1.19.1 on 2022-06-18
# Espressif ESP32-WROOM-32

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

class LedMatrix:
    def __init__(self, spi, cs_pins):
        # spi (machine.SPI): serial phripheral interface
        # cs_pins (tuple): elements of the tuple are instances of machine.Pin
        self.spi = spi
        self.cs_pins = cs_pins
        self.changedrow = set()
        self._initpins()
        self._initbuffer()
        self._initsettings()
    
    def _initpins(self):
        # prepare pins for communication between the MCU and max7219s
        self.spi.init(baudrate=10000000, polarity=0, phase=0, firstbit=self.spi.MSB)
        for cs_pin in self.cs_pins:
            cs_pin.init(mode=cs_pin.OUT, drive=cs_pin.DRIVE_0)
    
    def _initbuffer(self):
        # create the data structure of an empty buffer
        self.buffer = []
        for _ in range(8*len(self.cs_pins)):
            self.buffer.append(list("0"*8))
        self.buffer = tuple(self.buffer)
        
    def _initsettings(self):
        # prepare chips for matrices display
        self.test(0)
        self._intensity = 0
        self._writeall(INTENSITY, self._intensity)
        self._writeall(SCANLIMIT, 0x7)
        self._writeall(DECODEMODE, 0x0)
        self.clear()
        self.switch(1)

    def _writeall(self, addr, data):
        # write same data into each max7219
        for cs_pin in self.cs_pins:
            cs_pin.off()
        self.spi.write(bytearray([addr, data]))
        for cs_pin in self.cs_pins:
            cs_pin.on()
    
    def pixels(self, i, coords):
        # update led information in the buffer but not display
        for x, y in coords:
            self.buffer[y][x] = i
            self.changedrow.add(y)
    
    def refresh(self):
        # write data of rows with updated led according to the buffer and display
        for y in self.changedrow:
            cs, row = divmod(y, 8)
            self.cs_pins[cs].off()
            self.spi.write(bytearray([row+1, eval("0b"+"".join(self.buffer[y]))]))
            self.cs_pins[cs].on()
        self.changedrow.clear()
    
    def clearbuffer(self):
        # set the buffer to the initial state
        self._initbuffer()
        self.changedrow.clear()
    
    def directrow(self, cs, row, data):
        # directly write led data and show
        # the buffer is not altered
        self.cs_pins[cs].off()
        self.spi.write(bytearray([row, data]))
        self.cs_pins[cs].on()
    
    def clear(self):
        # directly turn off every LED
        # the buffer is not altered
        for i in range(8):
            self._writeall(DIGIT0+i, 0b00000000)
    
    def test(self, on):
        # turn on / off the led test mode
        if on == 1:
            self._writeall(DISPLAYTEST, 0x1)
        elif on == 0:
            self._writeall(DISPLAYTEST, 0x0)

    def intensity(self, mode, value=None):
        # adjust intensity and write the value into corresponding register
        if mode == 1 and self._intensity < 15:
            self._intensity += 1
        elif mode == 0 and self._intensity > 0:
            self._intensity -= 1
        elif mode == 2:
            self._intensity = value
        self._writeall(INTENSITY, self._intensity)
    
    def switch(self, state):
        # turn on \ off the power supply to each LED
        if state == 1:
            # switch on
            self._writeall(SHUTDOWN, 0x1)
        elif state == 0:
            # switch off
            self._writeall(SHUTDOWN, 0x0)