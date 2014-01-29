# coding=utf-8

"""
    BagOfWords.py
    
    This module implements a BagOfWords class, which maps words to occurrence count.
    
    @author David Greisler <s0531301@htw-berlin.de>

"""

class BagOfWords(object):
    """
    A bag of words, maps words to occurrence count in a document.
    
    A bag of words contains words extracted from a text. It stores words and how often they occurred
    in the text, but has no knowledge about the order of words/original text.
    
    When the constructor is called with a text as argument, it'll count the words in it and put them
    in the bag. Add more words with add_word(). It is also possible to merge bags using merge().
    
    Use number_of_words to get the total amount of words in the bag, number_of_distinct_words on the
    other hand, gives you only the amount of distinct words in the bag. Use count_word() to find out
    how often a specific word occurs in the bag. The method words() returns a dictionary mapping 
    words to occurrence count.
    
    """
    
    # Dictionary mapping words to occurrence count.
    _words = {}
    
    # Total number of words in the bag.
    _number_of_words = 0
    
    def __init__(self, text = ""):
        """
        Creates a new bag of words, containing all words from the given text.
        
        Args:
            text: Text to extract words from. Default: ""
        
        @todo Sanitize text before splitting, e.g. remove special characters like .!"§$%& ...
        """
        self._words = {}
        self._number_of_words = 0
        for word in text.split():
            self.add_word(word, 1)
    
    @property
    def number_of_words(self):
        """
        Returns the amount of words in the bag.
        
        """
        return self._number_of_words
    
    @property
    def number_of_distinct_words(self):
        """
        Returns the amount of distinct words in the bag.
        
        """
        return len(self._words)
    
    def count_word(self, word):
        """
        Returns the word count for the given word.
        
        Args:
            word: The word for which the count should be looked up.
           
        Returns:
            Number of occurrences of the given word.
        
        """
        count = 0
        
        if word in self._words:
            count = self._words[word]
        
        return count
    
    @property
    def words(self):
        """
        Returns a dictionary mapping words to occurrence count.
        
        Returns:
            Dictionary mapping words to occurrence count.
        
        """
        return self._words
    
    def merge(self, other_bag):
        """
        Merges the bag with the given bag and returns the result.
        
        Args:
            other_bag: The other bag of words.
            
        Returns:
            A bag of words containing all words from both bags.
        
        """
        result = BagOfWords("")
        result._number_of_words = self._number_of_words + other_bag._number_of_words
        
        for word in self._words:
            count_sum = self._words[word];
            
            if word in other_bag._words:
                count_sum += other_bag._words[word]
                
            result._words[word] = count_sum
        
        for word in other_bag._words:
            if word not in self._words:
                result._words[word] = other_bag._words[word]
              
        return result
    
    def add_word(self, word, amount = 1):
        """
        Adds the given word to the bag.
        
        Args:
            word: The word to add.
            amount: How many, default: 1
        
        """
        self._number_of_words += amount
        
        if word in self._words:
            self._words[word] += amount
        else:
            self._words[word] = amount
