# Raspberry Pi hotword voice assistant
(That could use a catchier name, couldn't it?)

A voice assistant, along the same vein as Amazon Echo and Google Home using
[Snowboy hotword detection](https://snowboy.kitt.ai/) for the voice activation.

This is really a pet project, so a lot of the commands here are heavily 
personalised for my use, but there's nothing really stopping anyone from modifying
it for theirs.


# Features
- Weather updates (using [Dark Sky](https://darksky.net/dev/) and 
[Google TTS](https://pypi.python.org/pypi/gTTS))
- News Flash briefing from BBC World News
- Philips Hue lights
- Wake-on-lan


# Dependancies:
- snowboy kitt.ai (Included as snowboy-linux or snowboy-pi, for Ubuntu and 
Raspberry Pi respectively)
- sudo apt-get install mpg321 wakeonlan libatlas3-base python-mutagen
- pip install qhue gTTS schedul pygame
