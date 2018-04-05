#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 16:50:44 2017

@author: apple
"""

import MapReduce
import sys

#The output should be a joined record: a single list of length 27 
#that contains the attributes from the order record 
#followed by the fields from the line item record. Each list element should be a string.

mr = MapReduce.MapReduce()

def mapper(record):
    # key: order_id
    # value: records
    key = record[1].encode("utf-8")
    
    mr.emit_intermediate(key,record )      ##return a dictionary of {order_id: records}, records is a list 

def reducer(key, list_of_values):  #each "order" record has a unique key, that's the point
    # key: order_id
    # value: records
    for record in list_of_values:
        if record[0]=="order":
            record_at_id=record   #record itself is already a list
            break  #get one record_at_id, should be only one order record for each key
    
    for record in list_of_values:
        if record[0]=="line_item":
            all_at_id=record_at_id+record  #get one all_at_id
            mr.emit(all_at_id)
        
        
        
        
        
if __name__ == '__main__':
    
   inputdata = open('records.json')
   #inputdata = open(sys.argv[1])
   mr.execute(inputdata, mapper, reducer)