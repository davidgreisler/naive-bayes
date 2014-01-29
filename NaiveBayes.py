# coding=utf-8

"""
    NaiveBayes.py
    
    @todo describe.
    
    @author David Greisler <s0531301@htw-berlin.de>

"""

from BagOfWords import BagOfWords
import math

class NaiveBayes(object):
    """
    
    """
    
    def compute_scores(self, document, vocabulary, classes):
        """
        
        """
        document_words = document.bag_of_words
        filtered_words = BagOfWords("")
        
        for word in document_words.words:
            if word in vocabulary.words:
                filtered_words.add_word(word, document_words.count_word(word))
        
        scores = {}
        for document_class in classes:
            scores[document_class] = math.log(document_class.prior_probability)
            
            for word in filtered_words.words:
                scores[document_class] += math.log(document_class.conditional_probability(word))

        return scores
