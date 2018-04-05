#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 23:16:20 2017

@author: apple
"""

import sys
import json

def cleanword(word):
    temp=word.lower()
    exclude=set([",","!","?",":",".", ";","@","#","=","...","//","*","_","~","/"," ' ","[","]","."])
    temp="".join(ch for ch in temp if not (ch in exclude))
    return temp

def term_freq_dict(json_file):
    
    with open(json_file) as f:
         tweets=f.readlines()
         termfreq={}
         totalcount=0
         
         for line in tweets:
             try:
                 mydict=json.loads(line)
                 tweetpiece=mydict[u'text'].encode('utf-8')
                 for word in tweetpiece.split():
                     totalcount+=1
                     word_cleaned=cleanword(word)
                     if word_cleaned in termfreq.keys():
                         termfreq[word_cleaned]+=1
                     else:
                         termfreq[word_cleaned]=1
                         
             except:
                continue
            
         for word in termfreq.keys():
             termfreq[word]=float(termfreq[word])/totalcount
             
    return termfreq


def main():
    json_file=sys.argv[1]
    #json_file='problem_1_submission.txt'
    a= term_freq_dict(json_file)

    for word in a.keys():
       sys.stdout.write(word+" "+str(a[word])+"\n")
        
if __name__=='__main__':
    main()
    
    
    
    