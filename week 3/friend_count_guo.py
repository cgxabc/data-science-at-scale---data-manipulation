#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 18:26:42 2017

@author: apple
"""

import MapReduce
import sys

#The output should be a joined record: a single list of length 27 
#that contains the attributes from the order record 
#followed by the fields from the line item record. Each list element should be a string.

mr = MapReduce.MapReduce()

def mapper(record):
    # key: person A
    # value: person A's friends
    
    key = record[0]
    mr.emit_intermediate(key, 1)     ##return a dictionary of {person A: 1,1,1,}, 

def reducer(key, list_of_values):  #each "order" record has a unique key, that's the point
    # key: person A
    # value: list of occurrence counts
    total = 0
    for v in list_of_values:
      total += v
    mr.emit((key, total))
        
        
        
        
if __name__ == '__main__':
    
   inputdata = open('friends.json')
   #inputdata = open(sys.argv[1])
   mr.execute(inputdata, mapper, reducer)