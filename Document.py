# coding=utf-8

"""
    Document.py
    
    This module implements a Document class which represents a document and contains a bag of words
    containing all words in the document.
    
    @author David Greisler <s0531301@htw-berlin.de>
    @author Paul Kitt <s0528516@htw-berlin.de>

"""

import io
from BagOfWords import BagOfWords

class Document(object):
    """
    Represents a document and provides a method to retrieve a bag of words containing all words in
    the document.
    
    """
    
    # Path of the document.
    _path = ""
    
    # Bag of words containing all words in the document.
    _bag_of_words = None
    
    def __init__(self, path):
        """
        Creates a new Document from the given path. Reads the text file at the given path and
        constructs a bag of words from it which can then be retrieved and used.
        
        Args:
            path: Path to the document.
        
        """
        self._path = path
        
        file_handle = io.open(self._path, 'r')
        self._bag_of_words = BagOfWords(file_handle.read().encode("utf-8"))
        file_handle.close()
    
    @property
    def path(self):
        """
        Returns the path of the document.
        
        """
        return self._path
    
    @property
    def bag_of_words(self):
        """
        Returns a bag of words containing all words from the document.
        
        Returns:
            Bag of words containing all words from the document.
        """
        return self._bag_of_words
