from gensim import corpora, models
import pyLDAvis.gensim
from pprint import pprint
from constants import *

corpus = corpora.MmCorpus(CORPUS_FILENAME)
dictionary = corpora.Dictionary.load(DICT_FILENAME)
lda = models.LdaModel.load(LDA_FILENAME)

pprint(lda.print_topics())
vis_data = pyLDAvis.gensim.prepare(lda, corpus, dictionary)
pyLDAvis.save_html(vis_data, VIS_FILENAME)


# pyLDAvis.display(vis_data)
