#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 18:26:42 2017

@author: apple
"""

import MapReduce
import sys


mr = MapReduce.MapReduce()

def mapper(record):
    # key: person A&friend sorted, so person&friend is the same as friend&person
    # value: person A, friend
    pair = [x.encode('utf-8').lower() for x in record]
    pair_mix=sorted(pair)
    key="&".join(pair_mix)
    mr.emit_intermediate(key, record)
    
  
   
def reducer(key, list_of_values): 
    #key: person&friend
    #list_of_values: [[,],[,]]
    count=0
    for pair in list_of_values:
        friend_pair=pair
        count+=1
    if count==1:
        mr.emit((friend_pair[1], friend_pair[0]))
        mr.emit((friend_pair[0], friend_pair[1]))
        
if __name__ == '__main__':
    
   inputdata = open('friends.json')
   #inputdata = open(sys.argv[1])
   mr.execute(inputdata, mapper, reducer)