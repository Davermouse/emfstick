import serial

ser = serial.Serial('/dev/tty.PL2303G-USBtoUART110')

print(ser.name)

ser.read_until(bytes.fromhex("80"), 20)

def fix_analog(val):
    if val > 128:
        return -(256 - val)
    else:
        return val

while True:
    out = ser.read(10)

    m_x = fix_analog(out[6])
    m_y = fix_analog(out[5])

    s_x = fix_analog(out[8])
    s_y = fix_analog(out[7])


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

    print (','.join([hex(i) for i in out]))
    print ("X:{} Y:{} X:{} Y: {}".format(m_x, m_y, s_x, s_y))
    print("Trigger_1st: {} Trigger_2nd: {} WR: {}".format(trigger_1st, trigger_2nd, weapon_release))
    print("AA Select Press: {} AA Select fwd: {} AA Select back: {}".format(aa_select_pre, aa_select_fwd, aa_select_bck))
    print("Paddle: {} NWS: {}".format(paddle, nws))
    print("Trim_r: {} Trim_l: {} Trim_u: {} Trim_d: {}\nCastle_r: {} Castle_l: {} Castle_u: {} Castle_d: {}".format(trim_r, trim_l, trim_u, trim_d, castle_r, castle_l, castle_u, castle_d))
    
    print("Secondary trigger press: {} left {} right {} button {}".format(secondary_trig_press, secondary_trig_left, secondary_trig_right, secondary_button))
    print("Secondary hat press: {} left {} right {} mid up: {} down: {} right up: {} down: {}".format(secondary_hat_press, secondary_hat_left, secondary_hat_right, secondary_mid_hat_up, secondary_mid_hat_down, secondary_right_up, secondary_right_down))
    print("Secondary left low press: {} up: {} down: {} up up {} down: {}".format(secondary_l_low_press, secondary_l_low_up, secondary_l_low_down, secondary_l_up_up, secondary_l_up_down))

ser.close()