import snowboy.snowboydecoder as snowboydecoder
import lights
import bash_scripts
import sam
import news
import os

interrupted = False
previous_command = ''


def init():

    hotword_models = []
    callbacks = []
    hotword_dict = {}
    main_model_folder = 'hotword_models'
    model_dir = os.listdir('hotword_models')

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
                'file': file_path
            }
            hotword_models.append(file_path)
            callbacks.append(
                lambda model=model: hotword_callback(
                    hotword_dict[model.split('.')[0]]
                )
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


# Check against the category - we can have multiple voice   models per category
def hotword_callback(keyword):
    play_confirmation_sound()
    global previous_command
    # Lights
    if keyword['category'] == 'lights':
        lights.toggle_lights()

    # Bash scripts
    elif keyword['category'] == 'computer':
        bash_scripts.wake_computer()
    elif keyword['category'] == 'screen_on':
        bash_scripts.screen_on()

    # SAM responses
    elif keyword['category'] == 'activation':
        sam.hotword_response()
    elif keyword['category'] == 'weather':
        sam.get_weather()

    # News briefing
    elif keyword['category'] == 'news':
        news.play()

    # Cancel previous commands
    elif (previous_command != 'cancel_that') \
            and (keyword['category'] == 'cancel'):
        hotword_callback(previous_command)

    previous_command = keyword


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
