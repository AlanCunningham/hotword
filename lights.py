from qhue import Bridge


# Move this to config file
user = 'ZQBKP98FFwl96iTsnDXrdvGfKMFUB8N40iMpJth9'
hue = Bridge('192.168.1.46', user)


def toggle_lights():
    if hue.lights[1]()['state']['on']:
        # Turn lights off
        # hue('lights', 1, 'state', on=False)
        hue.groups[1].action(on=False)
    else:
        # Turn lights on
        # hue('lights', 1, 'state', on=True)
        hue.groups[1].action(on=True)