import os


def wake_computer():
    mac_address = '90:2B:34:BC:20:1C'
    os.system('wakeonlan %s' % mac_address)


# Turn the Raspberry Pi touchscreen screen on - requires sudo
def screen_on():
    os.system('echo 0 | sudo tee /sys/class/backlight/*/bl_power')
