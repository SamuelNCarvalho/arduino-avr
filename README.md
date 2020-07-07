# AVR Arduino Core for WiFi Duck Project

This repository is a fork of the [AVR Arduino Core](https://github.com/arduino/ArduinoCore-avr) to include libraries, boards and modifications necessary to compile the [WiFi Duck](https://github.com/spacehuhntech/wifiduck) project.  
The goal of this is to have a simpler installation setup for anyone that likes to test, modify and contribute to the wifi duck project.  

## License and credits

Arduino IDE is developed and maintained by the Arduino team. The IDE is licensed under GPL.

## Modifications

* Removed unused variants
* Removed unused bootloaders
* Added [promicro bootloader](https://github.com/sparkfun/Arduino_Boards/tree/master/sparkfun/avr/bootloaders/caterina) to support 3.3V Atmega32u4
* Added boards.txt.py, modified boards.txt and platform.txt to add WiFi Duck boards and change default values
* Patched CDC.cpp to allow ESP8266 serial flashing through the atmega