# spotify-youtube
Playing with the spotify api and integrating with youtube

Both "SPOTIPY_CLIENT_ID" and "SPOTIPY_CLIENT_SECRET" environment variables need to be set with your [spotify developer creds](https://developer.spotify.com/dashboard/login) (You can put these in the .env file, or set them on the cli)

Install dependencies with `pip install -r requirements.txt`

Run the code with `python main.py`

The commands could be pip3 or python3 depending on how your python is set up.
## youtube-downloader-converter
Stolen from NeuralNine

A simple Python script that is able to download YouTube videos or playlists and convert them into MP3.

Copyright (c) NeuralNine 2020 - YouTube Downloader v0.2 Alpha

WARNING: DOWNLOADING COPYRIGHTED MATERIAL IS HIGHLY ILLEGAL!
I DO NOT TAKE ANY RESPONSIBILITY FOR YOUR USAGE OF THIS TOOL!
THIS IS FOR EDUCATIONAL PURPOSES ONLY!


## Spotify integration
The spotify function takes in a spotify playlist id (is part of the playlist url) and produces a list of youtube links for the tracks in the playlist.
The youtube downloader will then download these links.

The downloader will make a downloads folder and then put up to 4 copies of each track in the tracks respective folder.

This is a 'for fun' project. Do not attempt to use for non-learnings lol.
