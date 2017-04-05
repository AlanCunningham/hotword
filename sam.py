from gtts import gTTS
import urllib
import weather as forecast
from pygame import mixer
from mutagen.mp3 import MP3
import logging
import speech_recognition as sr


class Sam:

    activated = False
    preferred_phrases = []
    recogniser = sr.Recognizer()

    def __init__(self):
        logging.basicConfig(format='%(message)s', level=logging.INFO)
        # A list of phrases used by Google that will more likely be recognised
        # over similar sounding phrases
        self.preferred_phrases = [
            'news',
            'weather'
        ]

    # Default response to being activated
    def hotword_response(self):
        self.play_audio('hotword_response.mp3')
        activated = True

    def speech_recognition(self):
        print('Listening...')

        try:
            with sr.Microphone() as source:
                audio = self.recogniser.record(source, duration=2)

            result = self.recogniser.recognize_google(audio, language='en-GB').lower()
            self.play_audio('snowboy/resources/ding.wav')
            print('Recognised: %s' % result)

            if 'weather' in result:
                self.get_weather()
            elif 'news' in result:
                self.get_news()

        except sr.UnknownValueError:
            logging.error('Speech not recognised')
        except sr.RequestError:
            logging.error('Request error')
            self.speech_synthesis('Sorry, please try again')

    def speech_synthesis(self, text_to_say):
        language = 'en'
        tts = gTTS(text=text_to_say, lang=language)
        tts.save('tts.mp3')
        self.play_audio('tts.mp3')

    def get_weather(self):
        weather = forecast.Weather()
        daily_weather = weather.get_daily_weather()
        summary = daily_weather['summary']
        chance_of_rain = int(daily_weather['precipProbability'] * 100)
        full_weather = "Today will be %s with a %s percent chance of rain" \
                       % (summary, chance_of_rain)
        self.speech_synthesis(full_weather)

    def get_news(self):
        print('Downloading')
        news_url = 'http://wsdownload.bbc.co.uk/worldservice/css/96mp3/latest/bbcnewssummary.mp3'
        news_file = urllib.URLopener()
        news_file.retrieve(news_url, 'news.mp3')
        print('Finished')
        self.play_audio('news.mp3')

    def play_audio(self, file_path):
        audio_file = MP3(file_path)

        # Get the sample rate of the mp3 (could be different)
        sample_rate = audio_file.info.sample_rate
        mixer.init(sample_rate)
        mixer.music.load(file_path)
        mixer.music.play()

        try:
            # The sample_rate cannot be reset until mixer.quit() has been called
            while mixer.music.get_busy():
                # Check if audio is playing
                pass
        except Exception:
            pass
        self.stop_audio()

    def stop_audio(self):
        global activated
        try:
            mixer.music.stop()
            mixer.quit()
        except Exception:
            pass
        activated = False
