# coding=utf-8

"""
    main.py
    
    This module contains the main application logic of the naive bayes classificator.
    
    The application will look for training/test data under root_path. It expects a directory
    structure as follows:
    
    <root path>/<class name>/test/ containing test documents.
    <root path>/<class name>/train/ containing training documents.
    
    Class names have to be in the class_names list.
    
    The application will then use the training documents to train the classificator and subsequently
    classify the test documents using the trained naive bayes classificator. The resulting scores
    are written to stdout.
    
    @author David Greisler <s0531301@htw-berlin.de>
    @author Paul Kitt <s0528516@htw-berlin.de>
    
"""

from DirectoryCrawler import DirectoryCrawler 
from TrainingClass import TrainingClass
from NaiveBayes import NaiveBayes
from BagOfWords import BagOfWords
import os

root_path = "/home/david/Dokumente/Ausbildung/HTW Berlin/7. Semester/Aktuelle Themen der Informatik 2/Übung 2/data/"
crawler = DirectoryCrawler(root_path)
naive_bayes = NaiveBayes()

class_names = [ "politik", "sport", "wirtschaft" ]
training_classes = []
number_of_documents = 0
classes = []
vocabulary = BagOfWords("")

print "Root directory for test/training data: " + crawler.root_path
print "Class names: " + ', '.join(str(name) for name in class_names)

for document_class in class_names:
    training_class = TrainingClass(document_class, crawler.read_training_documents(document_class))
    training_classes.append(training_class)
    number_of_documents += len(training_class.training_documents)
    
    for document in training_class.training_documents:
        vocabulary = vocabulary.merge(document.bag_of_words)

print "Total number of documents: " + str(number_of_documents)
print "Words in vocabulary: " + str(vocabulary.number_of_distinct_words)
print

for training_class in training_classes:
    print ("* Training class '" + training_class.name + ""
           "' with " + str(len(training_class.training_documents)) + " training documents.")
    
    classes.append(training_class.train(number_of_documents, vocabulary))

print

for document_class in classes:
    print "Testing documents for '" + document_class.name + "'"
    
    documents = crawler.read_test_documents(document_class.name)
        
    for document in documents:
        scores = naive_bayes.compute_scores(document, vocabulary, classes)
        sorted_scores = sorted(scores, key = lambda c : scores[c], reverse = False)
        score_text = ', '.join(d_class.name + " (%.2f)" % scores[d_class] for d_class in sorted_scores)
        print "* '" + os.path.basename(document.path) + "': " + score_text
    
    print
