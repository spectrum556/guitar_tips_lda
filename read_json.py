import json
from pprint import pprint
import os
from os.path import join

FILENAME = 'songs.json'


def get_path(filename=FILENAME) -> str:
    current_path = os.path.dirname(__file__)
    resources = 'resources'
    return join(current_path, resources, filename)


def get_lyrics(path=get_path()) -> list:
    min_views = 7000
    texts = list()
    with open(path) as file:
        for line in file:
            artist = json.loads(line)
            for song in artist['songs']:
                if song['views'] > min_views:
                    texts.append(song['text'])
    return texts


if __name__ == '__main__':
    pprint(len(get_lyrics()))
