naive-bayes
===========
A naive-bayes classificator developed within the scope of a course work for AKTINF2.

The application will look for training/test data under a root path specified in main.py. It expects 
a directory structure as follows:
    
```<root path>/<class name>/test/ containing test documents.
<root path>/<class name>/train/ containing training documents.```
    
Class names have to be in the class_names in main.py list.
    
The application will then use the training documents to train the classificator and subsequently
classify the test documents using the trained naive bayes classificator. The resulting scores
are written to stdout.

Authors
=======
* David Greisler (s0531301)
* Paul Kitt (s0528516)

Requirements
============
None.
