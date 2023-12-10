import os
from pytube import YouTube

def download_video(url, path="videos_python"):
    yt = YouTube(url)
    video_stream = yt.streams.get_highest_resolution()

    if not os.path.exists(path):
        os.makedirs(path)

url = input("Colar o link do video:\n")