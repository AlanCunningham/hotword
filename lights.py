from qhue import Bridge
import ConfigParser

config = ConfigParser.ConfigParser()
config.read('config.py')
hue = Bridge(config.get('hue', 'bridge_ip'), config.get('hue', 'user'))


def toggle_lights():
    if hue.lights[1]()['state']['on']:
        # Turn lights off
        # hue('lights', 1, 'state', on=False)
        hue.groups[1].action(on=False)
    else:
        # Turn lights on
        # hue('lights', 1, 'state', on=True)
        hue.groups[1].action(on=True)


def full_brightness():
    hue.groups[1].action(bri=254, hue=8418, sat=140)


def dim_lights():
    hue.groups[1].action(bri=144, hue=7688, sat=199)
