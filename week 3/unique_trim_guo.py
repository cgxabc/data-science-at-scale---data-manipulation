#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 12:25:32 2017

@author: apple
"""


#Write a MapReduce query to remove the last 10 characters from each string of nucleotides, 
#then remove any duplicates generated.




import MapReduce
import sys


mr = MapReduce.MapReduce()

def mapper(record):
    # key: trimmed sequence
    # value: trimmed sequence
    key=record[1][:(len(record[1])-10)]
    
    mr.emit_intermediate(key, key)  #may be[key:key, key, key]
    
  
   
def reducer(key, list_of_values): 
    #key: key
    #list_of_values: key, key,key
    for key in list_of_values:
        mr.emit(key)
        break
        
        
    
        
if __name__ == '__main__':
    
   inputdata = open('dna.json')
   #inputdata = open(sys.argv[1])
   mr.execute(inputdata, mapper, reducer)