from gensim import corpora, models, similarities
from pprint import pprint
from constants import *


class Similar:
    def __init__(self):
        self.corpus = corpora.MmCorpus(CORPUS_FILENAME)
        self.dictionary = corpora.Dictionary.load(DICT_FILENAME)
        self.lda = lda = models.LdaModel.load(LDA_FILENAME)
        try:
            self.index = similarities.MatrixSimilarity.load(INDEX_FILENAME)
        except FileNotFoundError:
            self.index = self._make_index()

    def _make_index(self):
        """
        transform corpus to LDA space and index it
        """
        index = similarities.MatrixSimilarity(self.lda[self.corpus])
        index.save(INDEX_FILENAME)

    def get_similar_doc_numbers(self, number_in_dict, probability_threshold):
        """
        :return list of tuples (number of doc, similarity probability) for docs with
        probability higher probability_threshold
        """
        # convert the query to LDA space
        vec_lda = self.lda[self.corpus[number_in_dict]]

        # perform a similarity query against the corpus
        sims = self.index[vec_lda]
        sort_sims = sorted(enumerate(sims), key=lambda item: -item[1])
        return self._apply_threshold(sort_sims, probability_threshold, number_in_dict)

    def _apply_threshold(self, sims, threshold, number_in_dict):
        return [item for item in sims
                    if item[1] >= threshold and
                       item[0] != number_in_dict]
        # return list(filter(lambda item: item[1] >= threshold, sims))


if __name__ == '__main__':
    sims = Similar()
    print(sims.get_similar_doc_numbers(18, 0.95))
