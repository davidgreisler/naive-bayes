# coding=utf-8

"""
    DirectoryCrawler.py
    
    This module contains a DirectoryCrawler class, that reads documents from a test/training data
    directory and returns a list of documents.
    
    @author David Greisler <s0531301@htw-berlin.de>
    @author Paul Kitt <s0528516@htw-berlin.de>

"""

import os
from Document import Document

class DirectoryCrawler(object):
    """
    The directory crawler crawls through a directory containing test/training data and returns a
    list of documents for a given class name.
    
    The directory crawler expects the following directory layout:
    
    <root path>/<class name>/test/ containing test documents.
    <root path>/<class name>/train/ containing training documents.
    
    """
    
    # The path to the directory containing the test/training documents. Contains trailing slash.
    _root_path = ""
    
    def __init__(self, root_path):
        """
        Creates a new directory crawler using the given root path.
        
        """
        root_path = os.path.normpath(root_path) + os.sep
        
        self._root_path = root_path
    
    @property
    def root_path(self):
        """
        Returns the root path of the directory crawler.
        
        """
        return self._root_path
    
    @root_path.setter
    def root_path(self, root_path):
        """
        Sets the root path of the directory crawler.
        
        Args:
            root_path: The new root path.
        
        """
        root_path = os.path.normpath(root_path) + os.sep
        
        self._root_path = root_path
    
    def read_test_documents(self, document_class):
        """
        Reads all test documents for the given class name and returns them as list of documents.
        
        Returns:
            A list containing all test documents for the given class name.
        
        """
        documents = []
        
        document_paths = sorted(os.listdir(self._root_path + document_class + os.sep + "test"))
           
        for document_path in document_paths:
            full_path = self._root_path + document_class + os.sep + "test" + os.sep + document_path
            documents.append(Document(full_path))
        
        return documents
    
    def read_training_documents(self, document_class):
        """
        Reads all training documents for the given class name and returns them as list of documents.
        
        Returns:
            A list containing all training documents for the given class name.
        """
        documents = []
        
        document_paths = sorted(os.listdir(self._root_path + document_class + os.sep + "train"))
           
        for document_path in document_paths:
            full_path = self._root_path + document_class + os.sep + "train" + os.sep + document_path
            documents.append(Document(full_path))
        
        return documents
    
