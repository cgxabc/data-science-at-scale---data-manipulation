#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 00:06:43 2017

@author: apple
"""

import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    value = record[1]
    words = value.split()
    for w in words:
      mr.emit_intermediate(w, 1)  #{who: 1,1,1}, {this:1,1},...., self.intermediate is a dictionary.      

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    total = 0
    for v in list_of_values:
      total += v
    mr.emit((key, total))  #[who, 3], [this, 2], self.result is a list

# Do not modify below this line
# =============================
if __name__ == '__main__':
    
   inputdata = open('books.json')
   #inputdata = open(sys.argv[1])
   mr.execute(inputdata, mapper, reducer)