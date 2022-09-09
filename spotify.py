import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from bs4 import BeautifulSoup as soup
import urllib.request
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def get_playlist_song_urls(id):
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
    playlist = spotify.playlist(id)
    folder_name = (playlist['name'] + playlist['owner']['display_name']).replace(" ", "-")
    results = spotify.playlist_tracks(id)
    tracks = results['items']
    
    tracks_list = []
    for track in tracks:
        name = track['track']['name']
        artists = []
        for artist in track['track']['artists']:
            artists.append(artist['name'])
        album = track['track']['album']['name']
        print(name, artists, album)
        tracks_list.append((name, artists, album))

    tracks_links_list = []

    # Instantiate a webdriver
    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    except:
        print('Trying executable path')
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    
    for index, track in enumerate(tracks_list):
        name = track[0]
        print(f"{index} of {len(tracks_list}")
        artists = "+".join(track[1])
        url = f"https://www.youtube.com/results?search_query={name}+{artists}".replace(" ", "+")
       
        # Load the HTML page
        driver.get(url)

        # Parse processed webpage with BeautifulSoup
        page = soup(driver.page_source, "html.parser")
        
        links = list(map(lambda x: "youtube.com" + x['href'], page.findAll('a',attrs={'id':'video-title'})))[:4]
        tracks_links_list.append({"track_name": name, "artists": track[1], 'album': track[2], "links": links})
    driver.close()

    return tracks_links_list, folder_name


def connect_to_url(url): #Opening up connecting, grabbing the URL
    Uclient = urllib.request.urlopen(url)
    page_html = Uclient.read()
    Uclient.close()
    return(page_html)

if __name__ == "__main__":
    get_playlist_song_urls("6GLssFV1ZY0rZT68oITRXm?si")