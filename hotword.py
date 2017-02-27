import snowboy.snowboydecoder as snowboydecoder
import lights
import bash_scripts
import sam
import os

interrupted = False


def init():

    hotword_models = []
    callbacks = []
    model_files_dir = 'hotword_models/'
    model_files = os.listdir('hotword_models')

    # Find all models and create a list of callbacks
    for model in model_files:
        hotword_models.append(model_files_dir + model)
        callbacks.append(
            lambda model=model: hotword_callback(model.split('.')[0])
        )

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
    play_confirmation_sound()

    # Lights
    if keyword == 'lights':
        lights.toggle_lights()

    # Bash scripts
    elif keyword == 'computer':
        bash_scripts.wake_computer()
    elif keyword == 'screen_on':
        bash_scripts.screen_on()

    # SAM responses
    elif keyword == 'hey_sam':
        sam.hotword_response()
    elif keyword == 'weather' or keyword == 'whats_the_weather_like':
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
