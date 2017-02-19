import snowboy.snowboydecoder as snowboydecoder
import lights
import wol
import sam

interrupted = False


def init():
    hotword_models = [
        'hotword_models/Lights.pmdl',
        'hotword_models/computer.pmdl',
        'hotword_models/hey_sam.pmdl',
        'hotword_models/weather.pmdl',
        'hotword_models/whats_the_weather_like.pmdl',

    ]
    callbacks = [
        lambda: hotword_callback('lights'),
        lambda: hotword_callback('computer'),
        lambda: hotword_callback('hey_sam'),
        lambda: hotword_callback('weather'),
        lambda: hotword_callback('whats_the_weather_like'),
    ]
    sensitivity = [0.4]*len(hotword_models)

    # Setup hotword detector
    hotword_detector = snowboydecoder.HotwordDetector(
        hotword_models,
        sensitivity=sensitivity,
        audio_gain=1
    )

    hotword_detector.start(
        detected_callback=callbacks,
        interrupt_check=interrupt_callback,
        sleep_time=0.003,
    )


def hotword_callback(keyword):
    print('Keyword %s' % keyword)
    if keyword == 'lights':
        play_confirmation_sound()
        lights.toggle_lights()
    elif keyword == 'computer':
        play_confirmation_sound()
        wol.wake_computer()
    elif keyword == 'hey_sam':
        sam.say('What')
    elif keyword == 'weather' or keyword == 'whats_the_weather_like':
        play_confirmation_sound()
        sam.get_weather()


def play_confirmation_sound():
    snowboydecoder.play_audio_file(snowboydecoder.DETECT_DONG)


def signal_handler(signal, frame):
    global interrupted
    interrupted = True


def interrupt_callback():
    global interrupted
    return interrupted


if __name__ == '__main__':
    init()
