#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 12:02:08 2017

@author: apple
"""

import sys
import json

def cleanwords(word):
    temp=word.lower()
    exclude=set([",","!","?",":",".", ";","@","#","=","...","//","*","_","~","/"," ' ","[","]","."])
    temp="".join(ch for ch in temp if not (ch in exclude))  #combine characters one by one to form a new word
    return temp  ##return a new word
    

def count_hashtag(json_file):
    
    hash_counts_dict={}  #return a dictionary of hashtags and counts
    with open(json_file) as f:
        for line in f:
            try:
                 mydict=json.loads(line)
                 hashtags=mydict[u'entities']['hashtags']
                 for tag_data in hashtags:
                       tag_text=tag_data[u'text'].encode('utf-8')
                       tag_cleaned=cleanwords(tag_text)
                       if tag_cleaned in hash_counts_dict.keys():
                            hash_counts_dict[tag_cleaned]+=1
                       else:
                            hash_counts_dict[tag_cleaned]=1
            except:
                continue
            
    return hash_counts_dict
    
    
def main():
    
    json_file=sys.argv[1]
   # json_file='output.txt'
    hash_count=count_hashtag(json_file)
    hash_sort=sorted(hash_count.items(),key=lambda x:x[1], reverse=True)
   # print hash_sort
    
    if len(hash_sort)<10:
        top=len(hash_sort)
    else:
        top=10
        
        
    for i in range(top):
        hashtag=hash_sort[i][0]
        count=hash_sort[i][1]
        print hashtag+" "+str(count)
        
    

if __name__=='__main__':
    main()