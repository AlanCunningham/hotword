import snowboy.snowboydecoder as snowboydecoder
from qhue import Bridge

# Move this to config file
user = 'ZQBKP98FFwl96iTsnDXrdvGfKMFUB8N40iMpJth9'
hue = Bridge('192.168.1.46', user)


def init():
	print("Qhue: %s" % len(hue.lights()))
	# Setup hotword detector
	detector_lights_on = snowboydecoder.HotwordDetector(
		"Lights.pmdl", sensitivity=0.5, audio_gain=1
	)
	detector_lights_on.start(lights_callback)


def lights_callback():
	for light in hue.lights():
		if hue.lights[light]()['state']['on']:
			# Turn lights on
			hue('lights', light, 'state', on=False)
		else:
			# Turn lights off
			hue('lights', light, 'state', on=True)

if __name__ == "__main__":
	init()


