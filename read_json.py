import json
from pprint import pprint
from constants import *


class ReadJson:
    def __init__(self, songs_file_path, min_views):
        self.songs_file_path = songs_file_path
        self.min_views = min_views

    def get_lyrics(self) -> list:
        artists = []
        with open(self.songs_file_path) as file:
            for line in file:
                artist = json.loads(line)
                self.filter_popular(artist)
                artists.append(artist)
        self.filter_different(artists)
        texts = []
        for artist in artists:
            for song in artist['songs']:
                texts.append(song['text'])
        return texts

    def filter_popular(self, artist):
        """
        Mutates artist
        """
        songs = []
        for song in artist['songs']:
            if song['views'] > self.min_views:
                songs.append(song)
        artist['songs'] = songs
        return artist

    @staticmethod
    def filter_different(artists):
        """
        Mutates artists
        """
        song_texts = set()
        for artist in artists:
            artist_songs = set()
            songs = []
            for song in artist['songs']:
                if (song['text'] not in song_texts) and (song['name'] not in artist_songs):
                    songs.append(song)
                    song_texts.add(song['text'])
                    artist_songs.add(song['name'])
            artist['songs'] = songs
        return artists

if __name__ == '__main__':
    rj = ReadJson(SONGS_FILENAME, MIN_VIEWS)
    pprint(len(rj.get_lyrics()))
