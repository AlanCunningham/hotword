import os


def wake_computer():
    mac_address = '90:2B:34:BC:20:1C'
    os.system('wakeonlan %s' % mac_address)


# Turn the Raspberry Pi touchscreen screen on/off - requires sudo
def touchscreen_display(turn_on):
    if turn_on:
        command = 0
    else:
        command = 1
    os.system('echo %s | sudo tee /sys/class/backlight/*/bl_power' % command)
