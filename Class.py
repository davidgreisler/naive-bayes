# coding=utf-8

"""
    Class.py
    
    This module implements a Class class, which represents a document class for the Naive Bayes
    classificator.
    
    @author David Greisler <s0531301@htw-berlin.de>

"""

class Class(object):
    """
    Represents a class, has information about the prior probability of the class and maps words to
    the conditional probability that they occur in a document of this class.
    
    The prior_probability property contains the prior probability of the class, use the 
    conditional_probability(word) method to retrieve the probability for the given word or the 
    conditional_probabilities property to retrieve a dictionary mapping words to probability. 
    """
    
    # The name of the class.
    _name = ""
    
    # Dictionary mapping words to the computed conditional probability that the word occurs in a 
    # document of this class.
    _conditional_probabilities = {}
    
    # The prior probability of this class.
    _prior_probability = 0.0
    
    def __init__(self, name, prior_probability, conditional_probabilities = None):
        """
        Creates a new class with the given name, conditional probabilites and prior probability.
        
        Args:
            name: The name of the class.
            prior_probability: The prior probability of this class.
            conditional_probabilites: Dictionary mapping words to conditional probabilites.
        
        """
        
        if conditional_probabilities is None:
            conditional_probabilities = {}
        
        self._name = name
        self._conditional_probabilities = conditional_probabilities
        self._prior_probability = prior_probability
    
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
    def conditional_probabilites(self):
        """
        Returns a dictionary mapping words to the conditional probability that the word occurs in a 
        document of this class.
        
        Returns:
            Dictionary mapping words to conditional probabilities.
        
        """
        return self._conditional_probabilities
    
    def conditional_probability(self, word):
        """
        Returns the probability that the given word occurs in a document of this class.
        
        Returns:
            The probability that the given word occurs in a document of this class.
        
        @todo Is returning 0 if it doesn't exist correct here?
        
        """
        probability = 0
        
        if word in self._conditional_probabilities:
            probability = self._conditional_probabilities[word]
        
        return probability
            
    @property
    def prior_probability(self):
        """
        Returns prior probability of this class.
        
        """
        return self._prior_probability
    