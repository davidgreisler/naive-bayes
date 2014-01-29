# coding=utf-8

"""
    main.py
    
    @todo describe.
    @author David Greisler <s0531301@htw-berlin.de>
    
"""

from DirectoryCrawler import DirectoryCrawler 
from TrainingClass import TrainingClass
from NaiveBayes import NaiveBayes
from BagOfWords import BagOfWords

root_path = "<PATH TO data DIRECTORY>"
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
        print ("* '" + document.path + "': " 
               "" + ', '.join(d_class.name + " (" + str(scores[d_class]) + ")" for d_class in scores))
    
    print
