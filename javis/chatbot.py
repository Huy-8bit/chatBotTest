# crate chatbot


import logging
import os
import sys
import numpy as np
import random
import tensorflow as tf
import tflearn
import json
import nltk
from nltk.stem.lancaster import LancasterStemmer


import re
import os
import math
import os
import os.path
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

def preprocess(documents):
    # converting to lower case
    documents = [doc.lower() for doc in documents]
    # # removing numbers
    # documents = [re.sub(r'\d+', '', doc) for doc in documents]
    # # removing punctuation
    # documents = [re.sub(r'[^\w\s]', '', doc) for doc in documents]
    # removing stopwords
    stop_words = set(nltk.corpus.stopwords.words('english'))
    documents = [' '.join([word for word in doc.split()
                          if word not in stop_words]) for doc in documents]
    # removing whitespace
    documents = [doc.strip() for doc in documents]
    # tokenizing
    documents = [nltk.word_tokenize(doc) for doc in documents]
    # stemming
    stemmer = nltk.stem.PorterStemmer()
    documents = [[stemmer.stem(word) for word in doc] for doc in documents]
    return documents

data = input()

print(data)