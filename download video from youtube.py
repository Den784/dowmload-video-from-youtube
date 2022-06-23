from pytube import YouTube
from pyfiglet import Figlet

print(Figlet(font="slant").renderText("Download video"))

DOWNLIAD_FOLDER = 'F:\програмирование\Python\база\YouTube'

video_url = input('Ввеите ссылку: ')

video_obj = YouTube(video_url)

stream = video_obj.streams.get_highest_resolution()
stream.download(DOWNLIAD_FOLDER)
print(Figlet(font="slant").renderText("Done"))