import requests
import six
import lxml
from bs4 import BeautifulSoup
import argparse
import json
import os
import spotipy
import sys
import pprint

def get_lyrics(artist, song):
    '''Looks up song_url, parses page for lyrics and returns the lyrics.'''
    base_url = 'http://www.genius.com/'
    artist = artist
    song = song
    artist = artist.replace(' ', '-')
    song = song.replace(' ', '-')
    song_url = base_url + artist + '-' + song + '-lyrics'
    get_url = requests.get(song_url)
    song_soup = BeautifulSoup(get_url.text, 'lxml')
    soup_lyrics = song_soup.lyrics.text
    # for_removal = ['[Verse]', '[Verse 1]', '[verse]', '[Verse 1]', '[verse 1]', '[chorus]', '[Chorus]', '[Intro]', '[intro]', '[outro]', '[Outro]']
    # for x in for_removal:
    # 	if x in soup_lyrics:
    #         real_lyrics = soup_lyrics.replace(x, '')
    return soup_lyrics

def get_all_songs_from_artist(artist_id):
    birdy_uri = 'spotify:artist:' + artist_id
    spotify = spotipy.Spotify()

    results = spotify.artist_albums(birdy_uri, album_type='album')
    albums = results['items']
    while results['next']:
        results = spotify.next(results)
        albums.extend(results['items'])

    album_list = []
    for album in albums:
        album_list.append(album['name'])

    spotify.trace = False
    all_tracks_by_artist = []
    for album in album_list[1:]:
        album_results = spotify.search(q = "album:" + str(album), type = "album")

        # get the first album uri
        album_id = album_results['albums']['items'][0]['uri']

        # get album tracks
        tracks = spotify.album_tracks(album_id)
        for track in tracks['items']:
            all_tracks_by_artist.append(track['name'])
    return all_tracks_by_artist


artists = {'My bloody valentine':'3G3Gdm0ZRAOxLrbyjfhii5', 'Slowdive':'72X6FHxaShda0XeQw3vbeF', 'Mojave 3':'4jSYHcSo85heWskYvAULio', 'Chapterhouse':'3r94PF71LWRI5K6wqclNjQ'} # for reference/ knowing which bands I used
with open('shoegaze_lyrics_bank.txt', 'w') as lyrics:
    for key,_id_ in artists.items():
        songs = get_all_songs_from_artist(_id_)
        for song in songs:
            try: lyrics.write(get_lyrics(key, str(song)))
            except AttributeError:
                pass

# rename this file create_lyrics_bank.py
# make a main.py file to generate markovian phrases based on lyric bank
