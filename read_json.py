import json


class ReadJson:
    def __init__(self, songs_file_path, min_views):
        self.songs_file_path = songs_file_path
        self.min_views = min_views
        self.song_texts = []

    def get_song_texts(self) -> list:
        return self.song_texts

    def get_songs_count(self):
        return len(self.song_texts)

    def read_song_texts(self) -> list:
        artists = []
        with open(self.songs_file_path) as file:
            for line in file:
                artist = json.loads(line)
                self._filter_popular(artist)
                artists.append(artist)
        self._filter_different(artists)
        self.song_texts = []
        for artist in artists:
            for song in artist['songs']:
                self.song_texts.append(song['text'])
        return self.song_texts

    def _filter_popular(self, artist):
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
    def _filter_different(artists):
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
