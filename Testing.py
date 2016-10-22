from __future__ import print_function, division
import nltk
import os
import random
from collections import Counter
from nltk import word_tokenize, WordNetLemmatizer,sent_tokenize
from nltk.corpus import stopwords
from nltk import NaiveBayesClassifier, classify

stoplist = stopwords.words('english')
print(stopwords)
def func():

     lemmatizer = WordNetLemmatizer()
     return [lemmatizer.lemmatize(word.lower()) for word in word_tokenize(unicode("This is a very big line which is a collection of words!",errors='ignore'))  ]
     
print(str(func()))     
def get_features():
        return {word: count for word, count in Counter(func()).items() if not word in stoplist}
 
    
print(str(get_features()))     
