# OpenGameConsoleMK1
OpenGameConsoleMK1 is a simple open-sources handle game console based on micropython and esp32 with features of storing and editing configuration information and adjustable hardware properties (intensity and sound). Now an integrated version with PCB is available.

![](https://github.com/YikangLi2003/OpenGameConsoleMK1/blob/main/Show/integrated.jpg?raw=true)
![](https://github.com/YikangLi2003/OpenGameConsoleMK1/blob/main/Show/finished.png?raw=true)

## Setup with Wires

### List of Modules
* Espressif ESP32-WROOM-32 * 1
* 8x8 Led matrix powered by MAX7219 * 2
* 4-digit 8-segment LEDs powered by TM1650 with colon * 1
* 4-digit 8-segment LEDs powered by TM1650 without colon * 1
* Buzzer controlled by MOSFET activated by low level * 1
* 4-pin button * 6
* Voltage regulator module with 5V output * 1
* Battery capable of providing high enough voltage * 1

![](https://github.com/FreestyleCodeWarrior/OpenGameConsoleMK1/blob/main/Show/modules.jpg?raw=true)
![](https://github.com/FreestyleCodeWarrior/OpenGameConsoleMK1/blob/main/Show/connected.jpg?raw=true)

###  Connection of Modules
* **8x8 LED matrix - upside**

| Module | ESP32 GPIO |
| ------------- | ------------- |
| DIN | 13 |
| CLK | 14 |
| CS | 32 |

* **8x8 LED matrix - downside**

| Module | ESP32 GPIO |
| ------------- | ------------- |
| DIN | 13 |
| CLK | 14 |
| CS | 33 |

* **4-digit 8-segment LEDs with colon - upside**

| Module | ESP32 GPIO |
| ------------- | ------------- |
| SCL | 18 |
| SDA | 19 |

* **4-digit 8-segment LEDs without colon - downside**

| Module | ESP32 GPIO |
| ------------- | ------------- |
| SCL | 25 |
| SDA | 26 |

* **Buzzer**

| Module | ESP32 GPIO |
| ------------- | ------------- |
| Trigger | 0 |
| VCC | 3.3V |

* **Buttons**

| Module | ESP32 GPIO |
| ------------- | ------------- |
| UP  | 2 |
| DOWN  | 4 |
| LEFT  | 5 |
| RIGHT  | 22 |
| OK  | 23 |
| BACK  | 27 |

* **Battery**

| Battery | Voltage Regulator |
| ------------- | ------------- |
| +  | IN |
| -  | GND |

* **Voltage Regulator**

| Module | Other peripheral except buzzer|
| ------------- | ------------- |
| OUT | VCC |
| GND | GND |

![](https://github.com/FreestyleCodeWarrior/OpenGameConsoleMK1/blob/main/Show/wiring.png?raw=true)

## Setup with PCB

![](https://github.com/YikangLi2003/OpenGameConsoleMK1/blob/main/Show/PCB.png?raw=true)

### Upload of Firmware
1. Connect the esp32 to your PC
2. open thonny, select corresponding micropython interpreter and detect COM ports to get connection with micropython shell of MCU
3. Select all files in ***OpenGameConsoleMK1/Firmware/*** and upload to the root directory of the MCU
4. Remove cables from your PC then power on the MCU and other peripherals.

## Operation Instructions
### Input
![](https://github.com/FreestyleCodeWarrior/OpenGameConsoleMK1/blob/main/Show/input.jpg?raw=true)

Buttons shown above is the only hardware for inputing commands to the MCU.
Six buttons are assigned the following commands (some example functions are listed):
* **up/down**
Move to (when controlling a game character);
Go to other system page;
Increase/decrease selected quantitave values (such as time or level of intensity);
Turn on/off selected function;
...
* **left/right**
Move to (when controlling a game character);
Go to other system page;
Select game or setting item;
...
* **ok**
Fire, accelerate, etc. (when controlling a game character);
Enter the deep page from the current location;
...
* **back**
Back to the previous page from the current location;
Pause or quit game;
...

### Output
![](https://github.com/FreestyleCodeWarrior/OpenGameConsoleMK1/blob/main/Show/output.jpg?raw=true)
* **16x8 LED matrix** - graphic display
* **4-digit 8-segment LEDs with colon** - text and time display
* **4-digit 8-segment LEDs without colon** - text and score display
* **Buzzer** - sound output

### System Page Map
![](https://github.com/FreestyleCodeWarrior/OpenGameConsoleMK1/blob/main/Show/map_playgame.png?raw=true)
![](https://github.com/FreestyleCodeWarrior/OpenGameConsoleMK1/blob/main/Show/map_setconfiguration.png?raw=true)
