from qhue import Bridge


# Move this to config file
user = 'ZQBKP98FFwl96iTsnDXrdvGfKMFUB8N40iMpJth9'
hue = Bridge('192.168.1.46', user)


def toggle_lights():
    for light in hue.lights():
        if hue.lights[light]()['state']['on']:
            # Turn lights on
            hue('lights', light, 'state', on=False)
        else:
            # Turn lights off
            hue('lights', light, 'state', on=True)
