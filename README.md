# Raspberry Pi hotword voice assistant
(That could use a catchier name)

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
- sudo apt-get install mpg321 wakeonlan libatlas3-base python-mutagen libboost-all-dev
- pip install qhue gTTS schedul pygame face_recognition

# Setup
- Sign up for a [Dark Sky dev account](https://darksky.net/dev/)
- Update config.py with the following

```
[snowboy]
raspberry_pi: False  # Set to True if running on a Raspberry Pi

[hue]
user: your_hue_user_id
bridge_ip: your_hue_bridge_ip_address

[weather]
api_key: your_dark_sky_api_token
  location_lon: your_longitude
  location_lat: your_latitude
  units: uk2
  ```

# Running everything
From terminal, run `python hotword.py`

# Commands
Saying `Okay SAM` will activate the assistant and open up a set of secondary commands (a bit like saying "Okay Google"):
 - Weather
   - Any sentence with  the word `weather`
   - "What's the `weather` like?"
   - "Give me the `weather`"
- News headlines
  - Any sentence with `news` or `headlines`
  - "Play the `news`"
  - "What are today's `headlines`?"

Some commands can be said without needing to say `Okay SAM`:
- Lights
  - "Turn the lights on"
  - "Turn the lights off"
  - "Dim the lights"
  - "Full brightness"
  - "Everything off"
- Wake on LAN
  - "Computer"
- Stop command
  - "Cancel that"
  - "Stop playing"

You might find better results to record your own activation words on the [Snowboy Hotword Detection](https://snowboy.kitt.ai) website.  Hotword files (.pdml) can be placed in the `hotword_models` folder in the corresponding category folder.  For example, to add your own "Okay SAM" hotword:
- Record your activation hotword on the Snowboy website (doesn't need to be "Okay SAM" - it could be "Okay Google")
- Download the resulting .pdml file
- Save this file to hotword_models/activation/
- The file can be called anything (e.g. okay_google.pdml)
