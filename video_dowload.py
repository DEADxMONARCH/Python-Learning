from pytube import playlist
p = playlist("https://www.youtube.com/playlist?list=PLu0W_9lII9agpFUAlPFe_VNSlXW5uE0YL")

for video in p.videos:
    video.streams.first().download()