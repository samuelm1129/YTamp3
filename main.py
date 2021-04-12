import youtube_dl

#Se pide el link
input_url = input("Ingresa el link del video que deseas convertir: ")

#info   
video_info = youtube_dl.YoutubeDL().extract_info(url=input_url, download=False)
video_title = video_info['title']

#config
opciones = {
    'format': 'bestaudio/best',
    'outtmpl': f"C:/Users/Usuario/Downloads/musica/{video_title}.mp3",#aca tienes que poner donde quieres que quede tu MP3
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }]
}

#descarga
with youtube_dl.YoutubeDL(opciones) as ydl:
    ydl.download([input_url])
