from gensim import corpora
import re
from pprint import pprint  # pretty-printer
from collections import defaultdict
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import langid
from read_json import get_lyrics, get_path
from langdetect import detect
from pymystem3 import Mystem
from constants import *



LANGUAGE = 'ru'


class ElementsForLDA:
    def __init__(self, tokenize_documents):
        self.documents = tokenize_documents
        # build the dictionary where for each document each word has its own id
        self.dictionary = corpora.Dictionary(self.documents)
        # build the corpus: vectors with occurence of each word for each document
        self.corpus = [self.dictionary.doc2bow(doc) for doc in self.documents]

    def save_to_file(self):
        self.dictionary.save(DICT_FILENAME)
        token2id = self.dictionary.token2id
        print('Number of identical words: {}'.format(len(token2id)))
        pprint(token2id)

        # save corpus in Market Matrix format
        # this corpus can be loaded with corpus = corpora.MmCorpus('FILENAME.mm')
        corpora.MmCorpus.serialize(CORPUS_FILENAME, self.corpus)


class Preprocessor:
    def __init__(self, documents):
        self.documents = documents
        self.stopset = self.get_stopset()

    def run(self):
        self.pretokenize()
        self.make_tokenize()
        self.remove_lowfrequency_words()
        self.remove_stopwords()
        self.lemmetization()

    def pretokenize(self):
        self.remove_numbers()
        self.filter_lang()

    def filter_lang(self, lang=LANGUAGE):
        """
        Leaves documents, which in 'lang' language
        """
        self.documents = [doc for doc in self.documents if langid.classify(doc)[0] == lang]
        print('Number of documents: {}'.format(len(self.documents)))

    def remove_numbers(self):
        self.documents = [re.sub(r'[^\w\s]+|[\d]+',r'', doc)
                          for doc in self.documents]

    def make_tokenize(self):
        tokenizer = RegexpTokenizer(r'\w+')
        self.documents = [tokenizer.tokenize(doc.lower())
                          for doc in self.documents]

    def remove_lowfrequency_words(self, amount=3):
        frequency = defaultdict(int)
        # count all token
        for doc in self.documents:
            for token in doc:
                frequency[token] += 1
        # keep words that occur more than once
        self.documents = [[token for token in doc if frequency[token] > amount]
                          for doc in self.documents]

    def remove_stopwords(self):
        self.documents = [[word for word in doc if word not in self.stopset]
                          for doc in self.documents]

    def lemmetization(self):
        lemm = Mystem()
        self.documents = [[''.join(lemm.lemmatize(word)).replace('\n', '') for word in doc]
                          for doc in self.documents]

    def get_stopset(self) -> set:
        unigrams = [word for doc in self.documents for word in doc if len(word) == 1]
        bigrams = [word for doc in self.documents for word in doc if len(word) == 2]
        chords = Preprocessor.get_stopwords_from_file(CHORDS_FILENAME)

        user_stopwords = Preprocessor.get_stopwords_from_file(USER_WORDS_FILENAME)
        standart_stopwords = stopwords.words('russian') + \
                             stopwords.words('english') + \
                             Preprocessor.get_stopwords_from_file(UKRAINIAN_STOPWORDS_FILENAME)

        return set(unigrams + bigrams + standart_stopwords + chords + user_stopwords)

    @staticmethod
    def get_stopwords_from_file(filename) -> list:
        with open(get_path(filename)) as file:
            return [word.replace('\n', '').lower() for word in file]


# todo fix method
def remove_hightfrequency_lyrics(songs, amount=2):
    frequency = defaultdict(int)
    # count all token
    for song in songs:
        frequency[song] += 1
    pprint(frequency)
    # keep words that occur more than once
    return [song for song in songs if frequency[song] < amount]


if __name__ == '__main__':
    preprocessor = Preprocessor(get_lyrics())
    preprocessor.run()
    corp_and_dict = ElementsForLDA(preprocessor.documents)
    corp_and_dict.save_to_file()
