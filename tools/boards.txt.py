#!/usr/bin/env python3

boards = [
    {
        "id": "atmega32u4",
        "name": "Generic ATmega32u4",
        "preset": {},
        "pins": {
            0: "0 (RX Serial) [PD2]",
            1: "1 (TX Serial) [PD3]",
            2: "2 (SDA I2C) [PD1]",
            3: "3 (SCL I2C) [PD0]",
            4: "4 (A6) [PD4]",
            5: "5 [PC6]",
            6: "6 (A7) [PD7]",
            7: "7 [PE6]",
            8: "8 (A8) [PB4]",
            9: "9 (A9) [PB5]",
            10: "10 (A10) [PB6]",
            11: "11 [PB7]",
            12: "12 (A11) [PD6]",
            13: "13 [PC7]",
            14: "14 (MISO SPI) [PB3]",
            15: "15 (SCLK SPI) [PB1]",
            16: "16 (MOSI SPI) [PB2]",
            17: "17 (SS SPI) [PB0]",
            18: "18 (A0) [PF7]",
            19: "19 (A1) [PF6]",
            20: "20 (A2) [PF5]",
            21: "21 (A3) [PF4]",
            22: "22 (A4) [PF1]",
            23: "23 (A5) [PF0]",
        },
        "menu": {
            "cpu": True,
            "keyboard": True,
            "protocol": True,
            "debug": True,
            "led": True,
            "bridge": True,
            "bridge_button": True,
            "bridge_reset": True,
            "bridge_pin0": True,
        },
    },{
        "id": "dstike",
        "name": "DSTIKE WiFi Duck (ATmega32u4)",
        "preset": {
            "cpu": "16MHzatmega32U4",
            "protocol": "i2c",
            "led": 7,
            "bridge": "disabled",
        },
        "pins": {},
        "menu": {
            "keyboard": True,
            "debug": True,
        },
    },{
        "id": "leonardo",
        "name": "Arduino Leonardo",
        "preset": {
            "cpu": "16MHzatmega32U4",
        },
        "pins": {
            0: "0 (RX Serial)",
            1: "1 (TX Serial)",
            2: "2 (SDA I2C)",
            3: "3 (SCL I2C)",
            4: "4",
            5: "~5",
            6: "~6",
            7: "7",
            8: "8",
            9: "~9",
            10: "~10",
            11: "~11",
            12: "~12",
            13: "~13",
            14: "ICSP MISO (SPI)",
            15: "ICSP SCLK (SPI)",
            16: "ICSP MOSI (SPI)",
            18: "A0",
            19: "A1",
            20: "A2",
            21: "A3",
            22: "A4",
            23: "A5",
        },
        "menu": {
            "keyboard": True,
            "protocol": True,
            "debug": True,
            "led": True,
            "bridge": True,
            "bridge_button": True,
            "bridge_reset": True,
            "bridge_pin0": True,
        },
    },{
        "id": "micro",
        "name": "Arduino Micro",
        "preset": {
            "cpu": "16MHzatmega32U4",
        },
        "pins": {
            0: "RX (Serial)",
            1: "TX (Serial)",
            2: "2 (SDA I2C)",
            3: "3 (SCL I2C)",
            4: "4",
            5: "5",
            6: "6",
            7: "7",
            8: "8",
            9: "9",
            10: "10",
            11: "11",
            12: "12",
            13: "13",
            14: "MI (MISO SPI)",
            15: "SCK (SCLK SPI)",
            16: "MO (MOSI SPI)",
            17: "SS (SPI)",
            18: "A0",
            19: "A1",
            20: "A2",
            21: "A3",
            22: "A4",
            23: "A5",
        },
        "menu": {
            "keyboard": True,
            "protocol": True,
            "debug": True,
            "led": True,
            "bridge": True,
            "bridge_button": True,
            "bridge_reset": True,
            "bridge_pin0": True,
        },
    },{
        "id": "promicro",
        "name": "Sparkfun Pro Micro",
        "preset": {},
        "pins": {
            0: "RX (Serial)",
            1: "TX (Serial)",
            2: "2 (SDA I2C)",
            3: "3 (SCL I2C)",
            4: "4",
            5: "5",
            6: "6",
            7: "7",
            8: "8",
            9: "9",
            10: "10",
            14: "14",
            15: "15",
            16: "16",
            18: "A0",
            19: "A1",
            20: "A2",
            21: "A3",
        },
        "menu": {
            "cpu": True,
            "keyboard": True,
            "protocol": True,
            "debug": True,
            "led": True,
            "bridge": True,
            "bridge_button": True,
            "bridge_reset": True,
            "bridge_pin0": True,
        },
    },{
        "id": "cjmcu",
        "name": "CJMCU Beetle",
        "preset": {
            "cpu": "16MHzatmega32U4",
        },
        "pins": {
            0: "RX (Serial)",
            1: "TX (Serial)",
            2: "SDA (I2C)",
            3: "SCL (I2C)",
            9: "D9",
            10: "D10",
            11: "D11",
            14: "MI (MISO SPI)",
            15: "SCK (SCLK SPI)",
            16: "MO (MOSI SPI)",
            18: "A0",
            19: "A1",
            20: "A2",
        },
        "menu": {
            "keyboard": True,
            "protocol": True,
            "debug": True,
            "led": True,
            "bridge": True,
            "bridge_button": True,
            "bridge_reset": True,
            "bridge_pin0": True,
        },
    },{
        "id": "ssmicro",
        "name": "SS Micro",
        "preset": {
            "cpu": "8MHzatmega32U4",
        },
        "pins": {
            0: "D0 RX (Serial)",
            1: "D1 TX (Serial)",
            2: "D2 SDA (I2C)",
            3: "D3 SCL (I2C)",
            6: "D6 A8",
            9: "D9 A10",
            10: "D10 A11",
            11: "D11",
            14: "D14 MI (MISO SPI)",
            15: "D15 SCK (SCLK SPI)",
            16: "D16 MO (MOSI SPI)",
            18: "A0",
            19: "A1",
            20: "A2",
        },
        "menu": {
            "keyboard": True,
            "protocol": True,
            "debug": True,
            "led": True,
            "bridge": True,
            "bridge_button": True,
            "bridge_reset": True,
            "bridge_pin0": True,
        },
    },
]

menus = {
    "cpu": "Processor",
    "keyboardid": "USB Device ID",
    "protocol": "Protocol",
    "debug": "Debug",
    "ledpin": "Neopixel (WS2812b)",
    "bridge": "Serial Bridge",
    "bridgebutton": "Serial Bridge Enable Pin",
    "bridgerst": "Serial Bridge Reset Pin",
    "bridge0": "Serial Bridge GPIO-0 Pin",
}

defaults = {
    "upload": {
        "tool": "avrdude",
        "protocol": "avr109",
        "maximum_size": "28672",
        "maximum_data_size": "2560",
        "speed": "57600",
        "disable_flushing": "true",
        "use_1200bps_touch": "true",
        "wait_for_upload_port": "true",
    },
    "bootloader": {
        "tool": "avrdude",
        "unlock_bits": "0x3F",
        "lock_bits": "0x2F",
        "low_fuses": "0xFF",
        "high_fuses": "0xD8",
    },
    "build": {
        "board": "AVR_ATMEGA32U4",
        "core": "arduino",
#        "variant": "atmega32u4",
        "mcu": "atmega32u4",
    },
}

cpus = {
    "16MHzatmega32U4": {
        "name": "5V, 16 MHz",
        "f_cpu": "16000000L",
        "extended_fuses": "0xCB",
        "file": "caterina/Caterina-promicro16.hex",
    },
    "8MHzatmega32U4": {
        "name": "3.3V, 8 MHz",
        "f_cpu": "8000000L",
        "extended_fuses": "0xFE",
        "file": "caterina/Caterina-promicro8.hex",
    },
}

keyboards = {
    "default" : {
        "usb_manufacturer": "Arduino",
        "usb_product": "Leonardo",
        "vid": "0x2341",
        "pid": "0x8036",
    },
    "apple" : {
        "usb_manufacturer": "Apple",
        "usb_product": "Aluminium Keyboard",
        "vid": "0x05ac",
        "pid": "0x0221",
    },
    "appleint" : {
        "usb_manufacturer": "Apple",
        "usb_product": "Internal Keyboard/Trackpad",
        "vid": "0x05ac",
        "pid": "0x0259",
    },
    "logitechhid" : {
        "usb_manufacturer": "Logitech",
        "usb_product": "USB Keyboard",
        "vid": "0x046d",
        "pid": "0xc316",
    },
    "logitechgaming" : {
        "usb_manufacturer": "Logitech",
        "usb_product": "G910 Keyboard",
        "vid": "0x046d",
        "pid": "0xc335",
    },
    "ms" : {
        "usb_manufacturer": "Microsoft",
        "usb_product": "USB Keyboard",
        "vid": "0x045e",
        "pid": "0xfff8",
    },
}

protocols = {
    "auto": {
        "name": "Auto (I2C & Serial)",
        "flags": "-DENABLE_I2C -DENABLE_SERIAL",
    },
    "i2c": {
        "name": "I2C",
        "flags": "-DENABLE_I2C",
    },
    "serial": {
        "name": "Serial",
        "flags": "-DENABLE_SERIAL",
    },
}

debugs = {
    "serial": {
        "name": "Serial (115200b, newline)",
        "flags": "-DENABLE_DEBUG -DDEBUG_PORT=Serial -DDEBUG_BAUD=115200",
    },
    "disabled": {
        "name": "Disabled",
        "flags": "",
    },
}

bridges = {
    "disabled": {
        "name": "Disabled",
        "flags": "",
    },
    "serial1": {
        "name": "Serial1",
        "flags": "-DBRIDGE_ENABLE -DBRIDGE_PORT=Serial1",
    },
}

def menu_names():
    print("########## Generated boards.txt ##########")
    print()

    for i in menus:
        print(f"menu.{i}={menus[i]}")
    print()

def board_flags(id, name):
    print(f"########## {name} ##########")
    print()
    print(f"{id}.name={name}")
    print()

    for i in defaults['upload']:
        print(f"{id}.upload.{i}={defaults['upload'][i]}")
    print()

    for i in defaults['bootloader']:
        print(f"{id}.bootloader.{i}={defaults['bootloader'][i]}")
    print()

    for i in defaults['build']:
        print(f"{id}.build.{i}={defaults['build'][i]}")
    print(f"{id}.build.variant={id}")
    print()

def cpu_menu(id):
    print("# CPU #")

    for i in cpus:
        cpu = cpus[i]
        print(f"{id}.menu.cpu.{i}={cpu['name']}")
        print(f"{id}.menu.cpu.{i}.build.f_cpu={cpu['f_cpu']}")
        print(f"{id}.menu.cpu.{i}.bootloader.extended_fuses={cpu['extended_fuses']}")
        print(f"{id}.menu.cpu.{i}.bootloader.file={cpu['file']}")
        print()

def cpu_preset(id, value):
    print("# CPU #")

    cpu = cpus[value]
    print(f"{id}.build.f_cpu={cpu['f_cpu']}")
    print(f"{id}.bootloader.extended_fuses={cpu['extended_fuses']}")
    print(f"{id}.bootloader.file={cpu['file']}")
    print()

def keyboard_menu(id):
    print("# Keyboard ID #")

    for i in keyboards:
        keyboard = keyboards[i]
        print(f"{id}.menu.keyboardid.{i}={keyboard['usb_manufacturer']} {keyboard['usb_product']}")
        print(f"{id}.menu.keyboardid.{i}.build.vid={keyboard['vid']}")
        print(f"{id}.menu.keyboardid.{i}.build.pid={keyboard['pid']}")
        print(f"{id}.menu.keyboardid.{i}.build.usb_product={keyboard['usb_product']}")
        print(f"{id}.menu.keyboardid.{i}.build.usb_manufacturer={keyboard['usb_manufacturer']}")
        print()

def keyboard_preset(id, value):
    print("# Keyboard ID #")

    keyboard = keyboards[value]
    print(f"{id}.build.vid={keyboard['vid']}")
    print(f"{id}.build.pid={keyboard['pid']}")
    print(f"{id}.build.usb_product={keyboard['usb_product']}")
    print(f"{id}.build.usb_manufacturer={keyboard['usb_manufacturer']}")
    print()

def protocol_menu(id):
    print("# Protocol #")

    for i in protocols:
        protocol = protocols[i]
        print(f"{id}.menu.protocol.{i}={protocol['name']}")
        print(f"{id}.menu.protocol.{i}.build.protocol_flags={protocol['flags']}")
        print()

def protocol_preset(id, value):
    print("# Protocol #")

    protocol = protocols[value]
    print(f"{id}.build.protocol_flags={protocol['flags']}")
    print()

def debug_menu(id):
    print("# Debug #")

    for i in debugs:
        debug = debugs[i]
        print(f"{id}.menu.debug.{i}={debug['name']}")
        print(f"{id}.menu.debug.{i}.build.debug_flags={debug['flags']}")
        print()

def debug_preset(id, value):
    print("# Debug #")

    debug = debugs[value]
    print(f"{id}.build.debug_flags={debug['flags']}")
    print()

def pin_menu(id, pins, category, flag, value, exceptions):
    print(f"{id}.menu.{category}.disabled=Disabled")

    for pin in pins:
        if pin not in exceptions:
            print(f"{id}.menu.{category}.{pin}={pins[pin]}")
            print(f"{id}.menu.{category}.{pin}.build.{flag}={value}={pin}")
    print()

def pin_preset(id, flag, value, preset):
    print(f"{id}.build.{flag}={value}={preset}")
    print()

def led_menu(id, pins):
    print("# LED #")
    pin_menu(id, pins, "ledpin", "led_pin", "-DNEOPIXEL -DNEOPIXEL_NUM=1 -DLED_PIN", [])

def led_preset(id, value):
    print("# LED #")
    pin_preset(id, "led_pin", "-DNEOPIXEL -DNEOPIXEL_NUM=1 -DLED_PIN", value);

def bridge_menu(id):
    print("# Serial Bridge #")
    
    for i in bridges:
        bridge = bridges[i]
        print(f"{id}.menu.bridge.{i}={bridge['name']}")
        print(f"{id}.menu.bridge.{i}.build.bridge_flags={bridge['flags']}")
        print()

def bridge_preset(id, value):
    print("# Serial Bridge #")
    
    bridge = bridges[value]
    print(f"{id}.build.bridge_flags={bridge['flags']}")
    print()

def bridge_button_menu(id, pins):
    pin_menu(id, pins, "bridgebutton", "bridge_button", "-DBRIDGE_SWITCH", [0,1])

def bridge_button_preset(id, value):
    pin_preset(id, "bridge_button", "-DBRIDGE_SWITCH", value)

def bridge_reset_menu(id, pins):
    pin_menu(id, pins, "bridgerst", "bridge_rst", "-DBRIDGE_RST", [0,1])

def bridge_reset_preset(id, value):
    pin_preset(id, "bridge_rst", "-DBRIDGE_RST", value)

def bridge_pin0_menu(id, pins):
    pin_menu(id, pins, "bridge0", "bridge_0", "-DBRIDGE_0", [0,1])

def bridge_pin0_preset(id, value):
    pin_preset(id, "bridge_0", "-DBRIDGE_0", value)
    
menu_names()

for board in boards:
    board_flags(board['id'],board['name'])

    # Presets
    if "cpu" in board["preset"]:
        cpu_preset(board['id'], board["preset"]["cpu"])
    
    if "keyboard" in board["preset"]:
        keyboard_preset(board['id'], board["preset"]["keyboard"])

    if "protocol" in board["preset"]:
        protocol_preset(board['id'], board["preset"]["protocol"])
    
    if "debug" in board["preset"]:
        debug_preset(board['id'], board["preset"]["debug"])

    if "led" in board["preset"]:
        led_preset(board['id'], board["preset"]["led"])

    if "bridge" in board["preset"]:
        bridge_preset(board['id'], board["preset"]["bridge"])
    
    if "bridge_button" in board["preset"]:
        bridge_button_preset(board['id'], board["preset"]["bridge_button"])

    if "bridge_reset" in board["preset"]:
        bridge_reset_preset(board['id'], board["preset"]["bridge_reset"])

    if "bridge_pin0" in board["preset"]:
        bridge_pin0_preset(board['id'], board["preset"]["bridge_pin0"])

    # Menus
    if "cpu" in board["menu"]:
        cpu_menu(board['id'])

    if "keyboard" in board["menu"]:
        keyboard_menu(board['id'])

    if "protocol" in board["menu"]:
        protocol_menu(board['id'])

    if "debug" in board["menu"]:
        debug_menu(board['id'])

    if "led" in board["menu"]:
        led_menu(board['id'], board["pins"])

    if "bridge" in board["menu"]:
        bridge_menu(board['id'])

    if "bridge_button" in board["menu"]:
        bridge_button_menu(board['id'], board["pins"])

    if "bridge_reset" in board["menu"]:
        bridge_reset_menu(board['id'], board["pins"])

    if "bridge_pin0" in board["menu"]:
        bridge_pin0_menu(board['id'], board["pins"])