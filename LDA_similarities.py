from gensim import corpora, models, similarities
from constants import *
import json
import time
from pprint import pprint

STANDART_SIMILAR_AMOUNT = 50


class Similar:
    def __init__(self, id, similar_amount=STANDART_SIMILAR_AMOUNT, probability_threshold=0.0):
        self.id = id
        self.probability_threshold = probability_threshold
        self.similar_amount = similar_amount
        self.corpus = corpora.MmCorpus(CORPUS_FILENAME)
        self.dictionary = corpora.Dictionary.load(DICT_FILENAME)
        self.lda = models.LdaModel.load(LDA_FILENAME)
        try:
            self.index = similarities.MatrixSimilarity.load(INDEX_FILENAME)
        except FileNotFoundError:
            self.index = self._make_index()

        self.doc_ids = self._make_doc_ids()
        self.doc_ids = self.get_doc_ids()

    def _make_index(self):
        """
        transform corpus to LDA space and index id
        """
        index = similarities.MatrixSimilarity(self.lda[self.corpus])
        index.save(INDEX_FILENAME)
        return index
    def _make_doc_ids(self):
        """
        :return list of tuples (id of doc, similarity probability) for docs with
        probability higher probability_threshold
        """
        # convert the query to LDA space
        vec_lda = self.lda[self.corpus[self.id]]

        # perform a similarity query against the corpus
        sims = self.index[vec_lda]
        sort_sims = sorted(enumerate(sims), key=lambda item: -item[1])
        # perform a similarity query against the corpus
        return sort_sims

    def get_doc_ids(self):
        self._preprocessing()
        return self.doc_ids

    def _preprocessing(self):
        self._remove_self_id()
        self.doc_ids = self.doc_ids[:self.similar_amount]
        self._apply_threshold()

    def _apply_threshold(self):
        self.doc_ids = [item for item in self.doc_ids
                        if item[1] >= self.probability_threshold]

    def _remove_self_id(self):
        self.doc_ids = [item for item in self.doc_ids
                        if item[0] != self.id]

    def get_dict_list(self):
        return [
            {
                'song_id': item[0],
                'similar_degree': float(item[1])
            }
            for item in self.get_doc_ids()]

    def get_json(self):
        return json.dumps(self.get_dict_list())


if __name__ == '__main__':
    tic = time.time()
    sims = Similar(80, 50)
    tac = time.time()
    pprint(sims.get_dict_list())
    print((tac - tic) * 1000, 'ms')
