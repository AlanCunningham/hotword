from gtts import gTTS
import os
import weather as forecast


# Default response to "Hey Sam"
def hotword_response():
    os.system("mpg321 hotword_response.mp3")


def say(text_to_say):
    language = 'en'
    tts = gTTS(text=text_to_say, lang=language)
    tts.save("tts.mp3")
    os.system("mpg321 tts.mp3")


def get_weather():
    weather = forecast.Weather()
    daily_weather = weather.get_daily_weather()
    summary = daily_weather['summary']
    chance_of_rain = int(daily_weather['precipProbability'] * 100)
    full_weather = "Today will be %s with a %s percent chance of rain" \
                   % (summary, chance_of_rain)
    say(full_weather)
