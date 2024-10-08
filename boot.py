import supervisor
import usb_hid

supervisor.set_usb_identification("David Miles", "EMF Stick")
# This line doesn't seem to affect the name of the device in
# as seen by Windows
# usb_hid.set_interface_name('EMF Stick')

# This is based on the Adafruit example at 
# https://learn.adafruit.com/customizing-usb-devices-in-circuitpython/hid-devices#custom-hid-devices-3096614-9
GAMEPAD_REPORT_DESCRIPTOR = bytes((
    0x05, 0x01,  # Usage Page (Generic Desktop Ctrls)
    0x09, 0x05,  # Usage (Game Pad)
    0xA1, 0x01,  # Collection (Application)
    0x85, 0x04,  #   Report ID (4)

    0x05, 0x09,  #   Usage Page (Button)
    0x19, 0x01,  #   Usage Minimum (Button 1)
    0x29, 0x20,  #   Usage Maximum (Button 32)
    0x15, 0x00,  #   Logical Minimum (0)
    0x25, 0x01,  #   Logical Maximum (1)
    0x75, 0x01,  #   Report Size (1)
    0x95, 0x20,  #   Report Count (32)
    0x81, 0x02,  #   Input (Data,Var,Abs,No Wrap,Linear,Preferred State,No Null Position)

    0x05, 0x01,  #   Usage Page (Generic Desktop Ctrls)
    0x15, 0x81,  #   Logical Minimum (-127)
    0x25, 0x7F,  #   Logical Maximum (127)
    0x09, 0x30,  #   Usage (X)
    0x09, 0x31,  #   Usage (Y)
    0x09, 0x32,  #   Usage (Z)
    0x09, 0x35,  #   Usage (Rz)
    0x75, 0x08,  #   Report Size (8)
    0x95, 0x04,  #   Report Count (4)
    0x81, 0x02,  #   Input (Data,Var,Abs,No Wrap,Linear,Preferred State,No Null Position)

    0x05, 0x01,  #   Usage Page (Generic Desktop Ctrls)
    0x09, 0x39,  #   Hat switch
    0x15, 0x00,  #   Logical Minimum (0)
    0x25, 0x07,  #   Logical Maximum (7)
    0x75, 0x08,  #   Report size(8)
    0x95, 0x01,  #   Report count (1)
    0x65, 0x14,  #   Unit English Rotation/Angular Position 1 degree (Optional)
    0x81, 0x42,  #   Input             : Data, Var, Abs, Null State

    0xC0,        # End Collection
))

gamepad = usb_hid.Device(
    report_descriptor=GAMEPAD_REPORT_DESCRIPTOR,
    usage_page=0x01,           # Generic Desktop Control
    usage=0x05,                # Gamepad
    report_ids=(4,),           # Descriptor uses report ID 4.
    in_report_lengths=(9,),    # This gamepad sends 9 bytes in its report.
    out_report_lengths=(0,),   # It does not receive any reports.
)

usb_hid.enable(
    (usb_hid.Device.KEYBOARD,
     usb_hid.Device.MOUSE,
     usb_hid.Device.CONSUMER_CONTROL,
     gamepad,)
)

print("Booted EMF Stick")
