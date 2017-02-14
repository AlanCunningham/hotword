from wakeonlan import wol


def wake_computer():
    # Move this to a config item
    mac = '90:2B:34:BC:20:1C'
    print('Turning on computer')
    wol.send_magic_packet(mac)
