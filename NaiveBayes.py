# coding=utf-8

"""
    NaiveBayes.py
    
    This module implements the NaiveBayes class which contains a method to compute a score for each
    given class that rates the probability that a given document is in that class.
    
    @author David Greisler <s0531301@htw-berlin.de>

"""

from BagOfWords import BagOfWords
import math

class NaiveBayes(object):
    """
    This class implements the naive bayes scoring.
    
    Use the method compute_scores() with the document and classes to score.
    
    """
    
    def compute_scores(self, document, vocabulary, classes):
        """
        Computes a score for each given class that rates the probability that the given document is
        in that class.
        
        The algorithm first extracts the words from the document and counts the occurrence of each
        word. It ignores words that are not in the training vocabulary.
        
        Then the score for each class is initialied to the logarithm of it's prior score.
        
        For each class, the algorithm sums the logarithm of the conditional probability for every 
        word extracted from the document (excluding words not in the training vocabulary). The sum
        is added to the score.
        
        The scores are then multiplied by -1 to turn them to positive numbers. Lower scores are 
        better. 
        
        Args:
            document: The document which should be classified.
            vocabulary: The training vocabulary (words from all training documents).
            classes: The classes for which the scores should be computed.
        
        Returns:
            A dictionary mapping classes to scores. Lower score is better.
        
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
                scores[document_class] += filtered_words.count_word(word) \
                    * math.log(document_class.conditional_probability(word))

            scores[document_class] *= -1;
        
        return scores
