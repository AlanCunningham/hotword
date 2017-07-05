from gtts import gTTS
import logging
import speech_recognition as sr
import os
import audio_helper

recogniser = sr.Recognizer()


def recognition():
    global recogniser
    logging.info('Listening...')

    try:
        with sr.Microphone() as source:
            audio = recogniser.record(source, duration=2)

        result = recogniser.recognize_google(audio, language='en-GB').lower()
        os.system('play audio/confirmation.wav')
        print('Recognised: %s' % result)

        return result

    except sr.UnknownValueError:
        logging.warning('Speech not recognised')
        return False
    except sr.RequestError:
        logging.error('Request error')
        synthesis('Sorry, please try again')
        return False


def synthesis(text_to_say):
    language = 'en'
    tts = gTTS(text=text_to_say, lang=language)
    tts.save('tts.mp3')
    audio_helper.play_audio('tts.mp3')
