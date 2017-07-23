import os
from os.path import join


LDA_PARAMS = {'num_topics': 17,
              'passes': 30,
              'alpha': 0.001}


def get_path(dir_name, filename) -> str:
    current_path = os.path.dirname(__file__)
    return join(current_path, dir_name, filename)


PROJECT_PATH = os.path.dirname(__file__)
DIR_NAME = 'tmp'
VIS_DIR_NAME = 'results'
RESOURCES = 'resources'


CORPUS_FILENAME = get_path(DIR_NAME, 'songs.mm')
DICT_FILENAME = get_path(DIR_NAME, 'songs.dict')
LDA_FILENAME = get_path(DIR_NAME, 'songs.lda')

VIS_FILENAME = get_path(VIS_DIR_NAME, 'LDAvis {}.html'.format(LDA_PARAMS))

UKRAINIAN_STOPWORDS_FILENAME = get_path(RESOURCES, 'ukrainian-stopwords.txt')
CHORDS_FILENAME = get_path(RESOURCES, 'all_chords.txt')
USER_WORDS_FILENAME = get_path(RESOURCES, 'user_stopwords.txt')
