from gtts import gTTS
import os
import weather as forecast


def get_weather():
    weather = forecast.Weather()
    daily_weather = weather.get_daily_weather()
    say(daily_weather['summary'])

def say(text_to_say):
    language = 'en'
    tts = gTTS(text=text_to_say, lang=language)
    tts.save("speech.mp3")
    os.system("mpg321 speech.mp3")
