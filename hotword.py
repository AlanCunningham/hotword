import snowboy.snowboydecoder as snowboydecoder
import lights
import bash_scripts
from sam import Sam
import os
import thread

interrupted = False
previous_command = ''
sam = ''
hotword_detector = ''


def init():
    global sam
    hotword_models = []
    callbacks = []
    hotword_dict = {}
    main_model_folder = 'hotword_models'
    model_dir = os.listdir('hotword_models')
    sam = Sam()

    # Each voice model is stored in a category folder
    # e.g. hotword_models/weather/whats_the_weather_like.pdml
    # This section finds all categories and models to create a dictionary
    # of commands.
    for category in model_dir:
        cat = os.listdir(main_model_folder + '/' + category)
        # Model inside this category
        for model in cat:
            split_model = model.split('.')[0]
            file_path = main_model_folder + '/' + category + '/' + model
            hotword_dict[split_model] = {
                'category': category,
                'hotword': split_model,
                'file': file_path
            }
            hotword_models.append(file_path)
            callbacks.append(
                lambda model=model: thread.start_new_thread(
                    hotword_callback,
                    (hotword_dict[model.split('.')[0]],)
                )
            )

    sensitivity = [0.4]*len(hotword_models)

    # Setup hotword detector
    global hotword_detector
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




# Check against the category - we can have multiple voice models per category
def hotword_callback(keyword):
    global hotword_detector
    play_confirmation_sound()
    print('Hotword: %s' % keyword['hotword'])

    # Lights
    if keyword['category'] == 'lights':
        lights.toggle_lights()
    if keyword['category'] == 'turn_everything_off':
        lights.toggle_lights()
        bash_scripts.touchscreen_display(False)

    # Bash scripts
    elif keyword['category'] == 'computer':
        bash_scripts.wake_computer()
    elif keyword['category'] == 'screen_on':
        bash_scripts.touchscreen_display(True)

    # SAM responses
    elif keyword['category'] == 'activation':
        hotword_detector.terminate()
        sam.hotword_response()
        sam.speech_recognition()
        init()
    elif keyword['category'] == 'weather':
        sam.get_weather()
    elif keyword['category'] == 'news':
        sam.get_news()

    # Cancel previous commands
    elif keyword['category'] == 'cancel':
        sam.stop_audio()


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
