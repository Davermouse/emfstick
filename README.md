# EMFStick

A project to show how you can use a junk flightstick found in the [EMF Camp 2024](https://www.emfcamp.org) swapshop as a proper PC flightstick, with some handy examples of how to use a Pico as a PC game controller.

As featured in MagPi magazine #146 and at https://www.raspberrypi.com/news/raspberry-pi-pico-brings-junked-joysticks-back-to-life-the-magpi-146/

## Connecting from the PC

`emfstick_pc.py` contains some sample code to connect to the stick directly from a computer. This requires Python and pyserial.

## Connecting using a Raspberry Pi Pico

This project should work on any Pico device running CircuitPython. You would need to connect GP12 to TX and GP13 to RX, as configured in `code.py`

To deploy to a Pico, you can copy all the files in this repository onto your Pico device. The included `lib` folder includes the Adafruit [Adafruit_CircuitPython_HID](https://github.com/adafruit/Adafruit_CircuitPython_HID/tree/main) libraries which we use for HID communication.

`boot.py` - Configures the Pico as a USB HID game controller

`code.py` - Contains the main logic which reads the current state from the stick and sends updates as HID reports

`hid_gamepad.py` - An expanded version of the Adafruit example to support more buttons and joystick hats