import urllib
import weather as forecast
import logging
import speech_recognition as sr
import ConfigParser
import speech
import audio_helper


class Sam:

    preferred_phrases = []
    recogniser = sr.Recognizer()
    config = ConfigParser.ConfigParser()

    def __init__(self):
        logging.basicConfig(format='%(message)s', level=logging.INFO)
        self.config.read('config.py')
        # A list of phrases used by Google that will more likely be recognised
        # over similar sounding phrases
        self.preferred_phrases = [
            'news',
            'headlines',
            'weather'
        ]

    def second_level_commands(self):
        recognised_speech = speech.recognition()
        if recognised_speech:
            if 'weather' in recognised_speech:
                self.get_weather()
            elif any(news in recognised_speech for news in ['news', 'headline']):
                self.get_news()

    def get_weather(self):
        weather = forecast.Weather()
        daily_weather = weather.get_daily_weather()
        summary = daily_weather['summary']
        chance_of_rain = int(daily_weather['precipProbability'] * 100)
        full_weather = "Today will be %s with a %s percent chance of rain. %s" \
                       % (summary, chance_of_rain, weather.suggest_clothes())
        speech.synthesis(full_weather)

    def get_news(self):
        news_url = self.config.get('news', 'news_audio_url')
        news_file = urllib.URLopener()
        news_file.retrieve(news_url, 'news.mp3')
        audio_helper.play_audio('news.mp3')