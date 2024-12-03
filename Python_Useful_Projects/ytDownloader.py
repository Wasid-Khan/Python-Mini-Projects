from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

yd = yt.streams.get_highest_resolution()
yd.download('/downloads/')
print("Download Complete!")

