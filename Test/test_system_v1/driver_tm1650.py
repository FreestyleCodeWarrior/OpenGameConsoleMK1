# MicroPython version: v1.19.1 on 2022-06-18
# Espressif ESP32-WROOM-32

from micropython import const

# addresses of digit display unit
DIG = (const(0x68), const(0x6a), const(0x6c), const(0x6e))

# command for display settings
SETTING = const(0b01001000) 

# Levels of intensity
INT = (
    const((0,0,1)),
    const((0,1,0)),
    const((0,1,1)),
    const((1,0,0)),
    const((1,0,1)),
    const((1,1,0)),
    const((1,1,1)),
    const((0,0,0))
    )

POWERON = const(1) # power on led segments
POWEROFF = const(0) # power off led segments
SEG7 = const(1) # seven-segment mode: 1
SEG8 = const(0) # eight_segment mode: 0

# mapping of single character and display content
ENCODE = {
    " ":0,
    "0":63,
    "1":6,
    "2":91,
    "3":79,
    "4":102,
    "5":109,
    "6":125,
    "7":7,
    "8":127,
    "9":111,
    "A":119,
    "b":124,
    "C":57,
    "c":88,
    "d":94,
    "E":121,
    "F":113,
    "G":61,
    "H":118,
    "h":116,
    "I":6,
    "J":30,
    "K":118,
    "L":56,
    "M":85,
    "n":84,
    "O":63,
    "o":92,
    "P":115,
    "q":103,
    "r":80,
    "S":109,
    "t":120,
    "U":62,
    "u":28,
    "v":28,
    "X":118,
    "y":110,
    "Z":91
    }

class LedDigitalTube:
    def __init__(self, SoftI2C, scl, sda):
        self.si2c = SoftI2C(scl, sda, freq=10000000) # machine.SoftI2C object for communication
        self._intensity = 0
        self._segmode = SEG8
        self._state = POWERON
        self._set()        
        self.clear()
    
    def _write(self, byte_1, byte_2):
        # write one set of data into the chip
        self.si2c.start()
        self.si2c.write(bytearray([byte_1, byte_2]))
        self.si2c.stop()
    
    def _set(self):
        # set intensity, segment display mode and work state
        self._write(SETTING,\
        eval("0b0{}{}{}{}00{}".format(*INT[self._intensity], self._segmode, self._state)))
    
    def chars(self, c):
        # accept a string 4 characters long and display
        for pos in range(4):
            self._write(DIG[pos], ENCODE[c[pos]])
        
    def char(self, pos, c):
        # display one digit and its position then display
        self._write(DIG[pos], ENCODE[c])
    
    def segments(self, data):
        # accept display data in a list and display
        # no encoding
        # such as (0b00101001, 0b10100101, 0b10100101, 0b11001101)
        for pos in range(4):
            self._write(DIG[pos], data[pos])
    
    def segment(self, pos, data):
        # accept display data and position for only one set of led tubes then display
        # no encoding
        # such as pos=1, data=ob10101010
        self._write(DIG[pos], data)
    
    def clear(self):
        # turn off every led tube
        for pos in range(4):
            self._write(DIG[pos], 0)
    
    def intensity(self, mode, value=None):
        # adjust the intensity within 8 levels
        if mode == 1 and self._intensity < 7:
            self._intensity += 1
        elif mode == 0 and self._intensity > 0:
            self._intensity -= 1
        elif mode == 2:
            self._intensity = value
        self._set()
    
    def segmode(self, mode):
        # set display mode (8-segment or 7-segment)
        if mode == "7":
            self._segmode = SEG7
        elif mode == "8":
            self._segmode = SEG8
        self._set()
    
    def switch(self, state):
        # power on/off led tubes
        self._state = state
        self._set()
