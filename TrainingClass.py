# coding=utf-8

"""
    TrainingClass.py
    
    This module implements a TrainingClass class, which represents an untrained document class and
    provides a method to train it.
    
    @author David Greisler <s0531301@htw-berlin.de>

"""

from BagOfWords import BagOfWords
from Document import Document
from Class import Class

class TrainingClass(object):
    """
    This class represents a document class that has not yet been trained.
    
    It contains a list of training documents for the class and provides a method train() which
    trains it and returns a trained and ready-to-use Class object.
    
    """
    
    # The name of the class.
    _name = ""
    
    # List of training documents for this class.
    _training_documents = []
    
    def __init__(self, name, training_documents):
        """
        Creates a new training document with the given name using the given training documents.
        
        Args:
            name: Name of the class.
            training_documents: List of training documents for this class.

        """
        self._name = name
        self._training_documents = training_documents
    
    @property
    def name(self):
        """
        Returns the name of the class.
        
        """
        return self._name
    
    @name.setter
    def name(self, name):
        """
        Sets the name of this class to the given name.
        
        Args:
            name: The new name of this class.
        
        """
        self._name = name
    
    @property
    def training_documents(self):
        """
        Returns a list containing the training documents used to train this class.
        
        Returns:
            A list containing training documents for this class.
        
        """
        return self._training_documents
    
    @training_documents.setter
    def training_documents(self, training_documents):
        """
        Sets the training documents to use to train this class to the given ones.
        
        Args:
            training_documents: The documents to use for training this class.
        
        """
        self._training_documents = training_documents
        
    def train(self, number_of_documents, vocabulary):
        """
        Trains the class using the given number of total documents and the training documents to 
        compute conditional probabilites. Returns a trained Class.
        
        Args:
            number_of_documents: Total number of documents in the training documents set.
            vocabulary: The vocabulary of the training documents set (all training documents, not
                        just the ones for this class).
        
        Returns:
            A trained Class object, ready to use with the Naive Bayes classificator.
        
        """
        
        number_of_documents_in_class = len(self._training_documents)
        prior_probability = number_of_documents_in_class / float(number_of_documents)
        class_documents_words = BagOfWords("")
        
        for document in self._training_documents:
            class_documents_words = class_documents_words.merge(document.bag_of_words)
        
        conditional_probabilities = {}
        for word in vocabulary.words:
            if word not in conditional_probabilities:
                conditional_probabilities[word] = 0
            
            conditional_probabilities[word] += (class_documents_words.count_word(word) + 1) \
                / float(class_documents_words.number_of_words \
                        + class_documents_words.number_of_distinct_words)
                
        return Class(self._name, prior_probability, conditional_probabilities)
