# OpenGameConsoleMK1
OpenGameConsoleMK1 is a simple open-sources handle game console based on micropython and esp32 with features of storing and editing configuration information and adjustable hardware properties (intensity and sound).

## Setup

### List of Modules
* Espressif ESP32-WROOM-32 * 1
* 8x8 Led matrix powered by MAX7219 * 2
* 4-digit 8-segment LEDs powered by TM1650 with colon * 1
* 4-digit 8-segment LEDs powered by TM1650 without colon * 1
* Buzzer controlled by MOSFET activated by low level * 1
* 4-pin button * 6
* Voltage regulator module with 5V output * 1
* Battery capable of providing high enough voltage * 1

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

| Module | Other peripheral |
| ------------- | ------------- |
| OUT | VCC |
| GND | GND |


### Upload of Firmware
1. Connect the esp32 to your PC
2. open thonny, select corresponding micropython interpreter and detect COM ports to get connection with micropython shell of MCU
3. Select all files in ***OpenGameConsoleMK1/SourceCodes/*** and upload to the root directory of the MCU
4. Remove cables from your PC and power on the MCU and other peripherals.

## Operation Instructions
