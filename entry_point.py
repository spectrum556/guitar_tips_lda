from read_json import ReadJson
from constants import *
from tokenize_and_preprocessing import Preprocessor, ElementsForLDA


def run():
    rj = ReadJson(SONGS_FILENAME, MIN_VIEWS)
    rj.read_song_texts()
    print("Songs count: {}".format(len(rj.song_texts)))
    preprocessor = Preprocessor(rj.get_song_texts())
    preprocessor.run()
    corp_and_dict = ElementsForLDA(preprocessor.documents)
    corp_and_dict.save_to_file()

run()
