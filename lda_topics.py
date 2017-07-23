from gensim import corpora, models
from pprint import pprint
from constants import *


# Load the corpus and Dictionary
corpus = corpora.MmCorpus(CORPUS_FILENAME)
dictionary = corpora.Dictionary.load(DICT_FILENAME)

print("Running LDA with: {}".format(LDA_PARAMS))

lda = models.LdaModel(corpus,
                id2word=dictionary,
                num_topics=LDA_PARAMS['num_topics'],
                passes=LDA_PARAMS['passes'],
                alpha=LDA_PARAMS['alpha'])

print()
pprint(lda.print_topics())
lda.save(LDA_FILENAME)