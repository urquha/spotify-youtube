from spotify import get_playlist_song_urls
import youtube_downloader
import file_converter
import os
from mutagen.easyid3 import EasyID3
from dotenv import load_dotenv

def main():
    # id = input("Please input playlist Id\n")
    id = '1f001wcO6C52q5IT7yybxw'
    song_data = get_playlist_song_urls(id)
    try:
        os.mkdir('downloads')
    except:
        print("downloads exists already.")
    for song in song_data:
        artists = "_".join(song['artists'])
        song_name = song['track_name']
        folder_path = f"downloads/{artists}-{song_name}/"
        try:
            os.mkdir(folder_path)
        except:
            print(folder_path + " exists already.")
        for link in song['links']:
            filename = youtube_downloader.download_video(link, 'low', folder_path)
            file_converter.convert_to_mp3(folder_path + filename)
            os.remove(folder_path + filename)
            audio = EasyID3((folder_path + filename).replace(".mp4", ".mp3"))
            audio['title'] = song_name
            audio['artist'] = artists
            audio['album'] = song['album']
            audio.save()


if __name__ == "__main__":
    load_dotenv()
    main()