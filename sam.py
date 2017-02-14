from gtts import gTTS
import os


def say(text_to_say):
    language = 'en'
    tts = gTTS(text=text_to_say, lang=language)
    tts.save("speech.mp3")
    os.system("mpg321 speech.mp3")
