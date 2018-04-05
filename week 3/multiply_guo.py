#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 13:06:17 2017

@author: apple
"""

#The input to the map function will be a row of a matrix represented as a list.
# Each list will be of the form [matrix, i, j, value] 
#where matrix is a string and i, j, and value are integers.




import MapReduce
import sys


mr = MapReduce.MapReduce()

def mapper(record):
    # key: matrix id 
    # value: (i,j,value)
    key=record[0]
    if key=='a':
        mr.emit_intermediate(key, [record[1],record[2],record[3]]) #key: i,j,value
    else:
        mr.emit_intermediate(key, [record[2],record[1],record[3]]) #key: j,i,value
        
   
def reducer(key, list_of_values): 
    #key: a or b
    #list_of_value: a list of (i,j,value) or (j,i,value)
    a={}
    b={}
    
    if key=='a': #assign values to a_{i,j} and b_{i,j} 
        for v in list_of_values:  
            a[(v[0], v[1])]=v[2] 
        for v in mr.intermediate['b']:  
            b[(v[0], v[1])]=v[2] 
            
            
        for i in range(0,5):  
            for j in range(0,5):  
                if (i,j) not in a.keys():  
                    a[(i,j)]=0  
                if (j,i) not in b.keys():  
                    b[(j,i)]=0  
        result=0  #initialize sum
        #compute the multiplication A*Bij = SUM(Aik * Bkj) for k in 0..4  
        for i in range(0,5):  
            for j in range(0,5):  
                for k in range(0,5):  
                    result+=a[(i,k)]*b[(j,k)]  
                mr.emit((i,j,result))  
                result=0  #intialize sum again          
     
        
if __name__ == '__main__':
    
   inputdata = open('matrix.json')
   #inputdata = open(sys.argv[1])
   mr.execute(inputdata, mapper, reducer)