from pytube import YouTube

url_link = 'https://www.youtube.com/watch?v=2lAe1cqCOXo'#input('введите ссылку для скачивания: ')
try: 
    yt = YouTube(url_link)
except:
    print('неправильная ссылка'); exit   
avalable_audio_stream = yt.streams.filter(only_audio=True)
avalable_video_stream = yt.streams.filter(only_video=True)
avalable_progressiv_stream = yt.streams.filter(progressive=True)
amount_audio_streams = len(avalable_audio_stream)
amount_video_streams = len(avalable_video_stream)   
amount_progressive_streams = len(avalable_progressiv_stream)   
print('только видео {} потоков; только аудио {} потоков; и аудио и видео {} потоков'.format(amount_video_streams, amount_audio_streams, amount_progressive_streams))
choise1=input(' 1 - скачать видео трек\n 2 - скачать аудио трек\n 3 - скачать полный трек\n Выберите цифру: ')

if (int(choise1)==1):
    avalable_video_stream[0].download()
elif(int(choise1)==2):
    avalable_audio_stream[0].download()
elif(int(choise1)==3):
    avalable_progressiv_stream.get_lowest_resolution().download()


