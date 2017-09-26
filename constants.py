from helpers import *


LDA_PARAMS = {'num_topics': 17,
              'passes': 30,
              'alpha': 0.001}


DIR_NAME = 'tmp'
VIS_DIR_NAME = 'results'
RESOURCES = 'resources'


CORPUS_FILENAME = get_path(DIR_NAME, 'songs.mm')
DICT_FILENAME = get_path(DIR_NAME, 'songs.dict')
LDA_FILENAME = get_path(DIR_NAME, 'songs.lda')
INDEX_FILENAME = get_path(DIR_NAME, 'sims.index')

VIS_FILENAME = get_path(VIS_DIR_NAME, 'LDAvis {}.html'.format(LDA_PARAMS))

SONGS_FILENAME = get_path(RESOURCES,'songs.json')
UKRAINIAN_STOPWORDS_FILENAME = get_path(RESOURCES, 'ukrainian-stopwords.txt')
CHORDS_FILENAME = get_path(RESOURCES, 'all_chords.txt')
USER_WORDS_FILENAME = get_path(RESOURCES, 'user_stopwords.txt')

MIN_VIEWS = 7000
LANGUAGE = 'ru'

