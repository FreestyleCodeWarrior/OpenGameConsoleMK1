# Visual information for screen to show
# MicroPython version: v1.19.1 on 2022-06-18
# Espressif ESP32-WROOM-32


def diode():
    return (0b01111110,
            0b01000010,
            0b01011010,
            0b01011010,
            0b11111111,
            0b00100100,
            0b00100100,
            0b00000100)


def speaker():
    return (0b00000100,
            0b00010110,
            0b00110110,
            0b11110110,
            0b11110110,
            0b00110110,
            0b00010110,
            0b00000100)


def circle():
    return (0b00011000,
            0b00111100,
            0b01100110,
            0b11000011,
            0b11000011,
            0b01100110,
            0b00111100,
            0b00011000)


def cross():
    return (0b11000011,
            0b11100111,
            0b01111110,
            0b00111100,
            0b00111100,
            0b01111110,
            0b11100111,
            0b11000011)


def tool():
    return (0b01001001,
            0b01001001,
            0b01001001,
            0b01001111,
            0b11100110,
            0b11100110,
            0b11100110,
            0b11100110)


def disk():
    return (0b00011111,
            0b00100001,
            0b01000001,
            0b10000001,
            0b10111101,
            0b10100101,
            0b10100101,
            0b11111111)


def monster():
    return (0b00100100,
            0b00100100,
            0b01111110,
            0b11011011,
            0b11111111,
            0b11111111,
            0b10100101,
            0b00100100)


def fill():
    return tuple(0b11111111 for _ in range(8))


def empty():
    return tuple(0b00000000 for _ in range(8))


def indicator(up=False, down=False, left=False, right=False):
    rows = [0]
    
    if up:
        rows += [24, 24]
    else:
        rows += [0, 0]
        
    if left and right:
        rows += [102, 102]
    elif left:
        rows += [96, 96]
    elif right:
        rows += [6, 6]
    else:
        rows += [0, 0]
        
    if down:
        rows += [24, 24]
    else:
        rows += [0, 0]
        
    rows.append(0)
    
    return tuple(rows)
