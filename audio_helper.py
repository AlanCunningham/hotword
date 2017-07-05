from pygame import mixer
from mutagen.mp3 import MP3
import os
import thread


def play_audio(file_path):
    # Play audio on a separate thread so we can cancel it if we want to
    thread.start_new_thread(_play_audio, (file_path,))


def _play_audio(file_path):
    extension = file_path.split('.')[1]
    if extension == 'wav':
        os.system('play %s' % file_path)
    elif extension == 'mp3':
        # Playing MP3 files seems to be a bit more difficult.  The sample rate
        # from Google's speech synthesis and the news headlines are different,
        # so we need to find the sample rate and adjust the playback accordingly
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
        stop_audio()


def stop_audio():
    try:
        mixer.music.stop()
        mixer.quit()
    except Exception:
        pass