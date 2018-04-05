#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 14:39:17 2017

@author: apple
"""

#The input is a 2-element list: [document_id, text],
# where document_id is a string representing a document identifier
# and text is a string representing the text of the document. 

#The output should be a (word, document ID list) tuple 
#where word is a String and document ID list is a list of Strings.

import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

def mapper(record):
    # key: document identifier
    # value: text
    key = record[0]
    value = record[1]
    words = value.split()
    for w in words:
      mr.emit_intermediate(w, key)      ##return a dictionary of {word: doc1, doc2, doc3} 

def reducer(key, list_of_values):  
    # key: word
    # value: documents containing the word
    docs=set()
    for v in list_of_values:
      docs.add(v)   #set([doc1, doc2])
    list_doc=list(docs)  #convert set([doc1,doc2]) to [doc1, doc2]
    mr.emit((key, list_doc))  #return a list of [word, [doc1, doc2, doc3]]

if __name__ == '__main__':
    
   #inputdata = open('books.json')
   inputdata = open(sys.argv[1])
   mr.execute(inputdata, mapper, reducer)