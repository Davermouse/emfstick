# This is based on the example at 
# https://github.com/adafruit/Adafruit_CircuitPython_HID/blob/main/examples/hid_simple_gamepad.py

import board
import busio
import digitalio
import usb_hid

from hid_gamepad import Gamepad

print("")
print("Starting EMFStick")

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

gp = Gamepad(usb_hid.devices)
serial = busio.UART(tx = board.GP12, rx = board.GP13, timeout = 5, baudrate = 9600, bits = 8, stop = 1, parity = None, receiver_buffer_size = 64)

# Map a 2's complement 8-bit value to [-127-128]
def map_analog(val):
    if val > 128:
        return -(256 - val)
    else:
        return val

tick = 0

while True:
    tick = tick + 1

    print("Looking for sync")
    led.value = False

    while True:
        # Find the initial 0x80
        h = serial.read(1)

        if h == None:
            print("Error reading data")

        print(h)

        if h[0] == 0x80:
            break

    print("Found sync")
    led.value = True

    while True:
        out = serial.read(10)

        if out == None or out[9] != 0x80:
            break

        m_x = map_analog(out[6])
        m_y = map_analog(out[5])

        s_x = map_analog(out[8])
        s_y = map_analog(out[7])

        weapon_release = (out[0] & 1) == 1

        trim_r = (out[0] & 0x02) == 0x02
        trim_u = (out[0] & 0x04) == 0x04
        trim_l = (out[0] & 0x08) == 0x08
        trim_d = (out[0] & 0x10) == 0x10

        castle_r = (out[0] & 0x20) == 0x20
        castle_u = (out[0] & 0x40) == 0x40
        castle_l = (out[1] & 0x01) == 0x01
        castle_d = (out[1] & 0x02) == 0x02

        paddle = (out[1] & 0x04) == 0x04

        trigger_1st = (out[1] & 0x08) == 0x08

        aa_select_pre = (out[1] & 0x10) == 0x10
        aa_select_fwd = (out[1] & 0x20) == 0x20
        aa_select_bck = (out[1] & 0x40) == 0x40

        nws = (out[2] & 0x01) == 0x01

        secondary_hat_press = (out[2] & 0x02) == 0x02
        secondary_hat_left = (out[2] & 0x04) == 0x04
        secondary_hat_right = (out[2] & 0x08) == 0x08

        secondary_mid_hat_up = (out[2] & 0x10) == 0x10
        secondary_mid_hat_down = (out[2] & 0x20) == 0x20

        secondary_right_up = (out[2] & 0x40) == 0x40
        secondary_right_down = (out[3] & 0x01) == 0x01

        secondary_button = (out[3] & 0x02) == 0x02

        secondary_trig_press = (out[3] & 0x04) == 0x04
        secondary_trig_left = (out[3] & 0x08) == 0x08
        secondary_trig_right = (out[3] & 0x10) == 0x10

        secondary_l_low_press = (out[3] & 0x20) == 0x20
        secondary_l_low_up = (out[3] & 0x40) == 0x40
        secondary_l_low_down = (out[4] & 0x01) == 0x01
        secondary_l_up_up = (out[4] & 0x02) == 0x02
        secondary_l_up_down = (out[4] & 0x04) == 0x04

        trigger_2nd = (out[4] & 0x08) == 0x08

        gp.move_joysticks(
            x=m_x,
            y=m_y,
            z=s_x,
            r_z=s_y
        )

        pressed = []
        released = []

        if trigger_1st:
            pressed.append(1)
        else:
            released.append(1)

        if trigger_2nd:
            pressed.append(2)
        else:
            released.append(2)

        if weapon_release:
            pressed.append(3)
        else:
            released.append(3)

        if trim_r:
            pressed.append(4)
        else:
            released.append(4)

        if trim_u:
            pressed.append(5)
        else:
            released.append(5)

        if trim_l:
            pressed.append(6)
        else:
            released.append(6)

        if trim_d:
            pressed.append(7)
        else:
            released.append(7)

        if castle_r:
            pressed.append(8)
        else:
            released.append(8)

        if castle_u:
            pressed.append(9)
        else:
            released.append(9)

        if castle_l:
            pressed.append(10)
        else:
            released.append(10)

        if castle_d:
            pressed.append(11)
        else:
            released.append(11)

        if aa_select_pre:
            pressed.append(12)
        else:
            released.append(12)

        if aa_select_bck:
            pressed.append(13)
        else:
            released.append(13)

        if aa_select_fwd:
            pressed.append(14)
        else:
            released.append(14)

        if nws:
            pressed.append(15)
        else:
            released.append(15)

        if paddle:
            pressed.append(16)
        else:
            released.append(16)

        if secondary_trig_press:
            pressed.append(17)
        else:
            released.append(17)

        if secondary_trig_left:
            pressed.append(18)
        else:
            released.append(18)

        if secondary_trig_right:
            pressed.append(19)
        else:
            released.append(19)

        if secondary_hat_press:
            pressed.append(20)
        else:
            released.append(20)
        if secondary_hat_left:
            pressed.append(21)
        else:
            released.append(21)
        if secondary_hat_right:
            pressed.append(22)
        else:
            released.append(22)

        if secondary_mid_hat_up:
            pressed.append(23)
        else:
            released.append(23)
        if secondary_mid_hat_down:
            pressed.append(24)
        else:
            released.append(24)

        if secondary_right_up:
            pressed.append(25)
        else:
            released.append(25)
        if secondary_right_down:
            pressed.append(26)
        else:
            released.append(26)

        if secondary_button:
            pressed.append(27)
        else:
            released.append(27)

        if secondary_l_up_up:
            pressed.append(28)
        else:
            released.append(28)
        if secondary_l_up_down:
            pressed.append(29)
        else:
            released.append(29)
        if secondary_l_low_press:
            pressed.append(30)
        else:
            released.append(30)
        if secondary_l_low_up:
            pressed.append(31)
        else:
            released.append(31)
        if secondary_l_low_down:
            pressed.append(32)
        else:
            released.append(32)

        gp.press_buttons(*pressed)
        gp.release_buttons(*released)
        #print(" x", ax.value, "y", ay.value)
