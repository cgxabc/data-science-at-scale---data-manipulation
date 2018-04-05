#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 11:41:30 2017

@author: apple
"""

import sys
import json

def sentimentscoredic(affinfile):
    
    global scores
    scores={}
    with open(affinfile) as f:
        for line in f:
            term,score=line.split('\t')
            scores[term]=int(score)
    return scores
   # print scores
            
def tweetsentiscore(tweettext):
    tweetscore=0
    for word in tweettext:
         if word in scores.keys():   ##using prescored dictionary
             tweetscore+=scores[word]
    return tweetscore


def score_tweetfile(json_file):
    
     with open(json_file) as twitter_file:
           tweets=twitter_file.readlines()
           for line in tweets:
                try:
                    tweetdic=json.loads(line)  #loads for string, load for file
                    tweet=tweetdic[u'text']
                    sentiment=tweetsentiscore(tweet.split())
                    sys.stdout.write(str(sentiment)+"\n")  #need to convert to strings, and print line by line
                except:
                   continue
         
            
            
def main():
    
    #affinfile=sys.argv[1]
    #json_file=sys.argv[2]
    affinfile='AFINN-111.txt'
 
    sentimentscoredic(affinfile)
    
    json_file='output.txt'
    score_tweetfile(json_file)
    
    
if __name__ == '__main__':
    main()
    
    
    
    
    