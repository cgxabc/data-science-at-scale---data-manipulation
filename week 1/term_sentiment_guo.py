#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 09:21:23 2017

@author: apple
"""

import sys
import json



def predictionary(pre_file):
    ##we want to make each line of the pre-file a dictionary
    word_score={}
    with open(pre_file) as f:
        for line in f:
            term,score=line.split("\t")
            word_score[term]=int(score)
    return word_score    
            
       

def cleanwords(word):
    temp=word.lower()
    exclude=set([",","!","?",":",".", ";","@","#","=","...","//","*","_","~","/"," ' ","[","]","."])
    temp="".join(ch for ch in temp if not (ch in exclude))  #combine characters one by one to form a new word
    return temp  ##return a new word
    

def score_tweet(tweet, pre_dict):
    score_a_piece=0
    for word in tweet:  # a set of words like "I", "love", "icecream"
        word_cleaned=cleanwords(word)
        if word_cleaned in pre_dict.keys():
            score_a_piece+=pre_dict[word_cleaned]
    return score_a_piece
    


    
def score_file(in_file, pre_dict):
    ##return a dictionary of tweets and scores,given a json file###
    file_dict={}
    with open(in_file) as f:  #need to open the file first
        tweets=f.readlines()  # read each line
        for line in tweets:
            try:
                mydict=json.loads(line)  # each line is a dictionary, we need the keys which are the tweets
                tweet=mydict[u'text'].encode('utf-8')
                sentiment=score_tweet(tweet.split(),pre_dict)  #tweet.split() is a set of words
                if sentiment!=0:  # this step is crucial, we only record tweets with nonzero sentiment
                     file_dict[tweet]=sentiment
                
            except:
                continue
    return file_dict
    
    
    
def score_new_words(in_file_dic, pre_dict):
    ##for each new word in file, compute the ratio of the score of the tweet 
    #in which the new word is in to the length of the tweet, then add all such ratios for all the tweets
    #in which the new word is in. Return a new dictionary of new words and their scores
    new_words_dict={}
    for tweets in in_file_dic:  # we already have a dictionary with keys being tweets
        sentiment=in_file_dic[tweets]
        for word in tweets.split():
            word_cleaned=cleanwords(word)
            if not (word_cleaned in pre_dict.keys()):
                if word_cleaned in new_words_dict.keys():
                    new_words_dict[word_cleaned]+=float(sentiment)/len(tweets)
                else:
                    new_words_dict[word_cleaned]=float(sentiment)/len(tweets)
    return new_words_dict
    
                
            
   
def main():
    
     pre_file=sys.argv[1] 
     in_file=sys.argv[2]
     #pre_file='AFINN-111.txt'
    # in_file='output.txt'
     pre_dict= predictionary(pre_file)
     in_file_dic=score_file(in_file,pre_dict)
     new_words_dict=score_new_words(in_file_dic,pre_dict)
     for word in new_words_dict.keys():
         print word+" "+str(new_words_dict[word])
   #  for tweet in in_file_dic.keys():
   #      print tweet+" "+str(in_file_dic[tweet])
     #    sys.stdout.write(tweet + " " + str(scorefile[tweet])+"\n")  the same as above
    # for word in pre_dict.keys():
    #     print word+" "+pre_dict[word]
    
    
    
if __name__=='__main__':
    main()
    
    