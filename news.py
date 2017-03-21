import urllib
import os


def play():
    print('Downloading')
    news_url = 'http://wsdownload.bbc.co.uk/worldservice/css/96mp3/latest/bbcnewssummary.mp3'
    news_file = urllib.URLopener()
    news_file.retrieve(news_url, 'news.mp3')
    print('Finished')
    os.system("mpg321 news.mp3")