#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 22:50:50 2017

@author: apple
"""

import json

class MapReduce:
    
    def __init__(self):
        self.intermediate = {}  #this is a dictionary
        self.result = []  #this is a list

    def emit_intermediate(self, key, value):
        self.intermediate.setdefault(key, [])
        self.intermediate[key].append(value)  #self.intermediate[key] is a list of values.

    def emit(self, value):
        self.result.append(value)  #append to a list

    def execute(self, data, mapper, reducer):
        for line in data:
            record = json.loads(line)
            
            mapper(record) #use mapper function, return a dictionary

        for key in self.intermediate:
            
            reducer(key, self.intermediate[key])  #use reducer function, return a list

        #jenc = json.JSONEncoder(encoding='latin-1')
        jenc = json.JSONEncoder()  ###change from json to python
        for item in self.result:
            print jenc.encode(item)