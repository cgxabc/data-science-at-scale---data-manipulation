#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 22:58:15 2017

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
 


def get_state(location):
    
    states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
        }
    
    if "," in location:
        statecode=location.split(", ")[1]  #it's ", "instead of ",", there's a blank after ","!
        if statecode.upper() in states.keys():
            return statecode.upper()
        else:
            return False
    else:
        return False
    
    
 
    
def score_file(in_file, pre_dict):
    
   # state_score_dict={}  ##return a dictionary of states and state scores,given a json file###
   # state_count_dict={}  ##return a dictionary of states and state counts, given a json file###
   # state_sentiment_dict={} #return a dictionary of states and average scores, given a json file###
    
    with open(in_file) as f:  #need to open the file first
    
        tweets=f.readlines()  # read each line
        state_score_dict={}  ##return a dictionary of states and state scores,given a json file###
        state_count_dict={}  ##return a dictionary of states and state counts, given a json file###
              
        for line in tweets:
            try:
                mydict=json.loads(line)  # each line is a dictionary, we need the keys which are the tweets
                loc = mydict[u'user'][u'location'].encode('utf-8') #get the location
                state = get_state(loc) #find the state
                
                if state!=False: 
                    tweet=mydict[u'text'].encode('utf-8')
                    sentiment=score_tweet(tweet.split(),pre_dict)  #tweet.split() is a set of words
                    
                    if state.upper() in state_score_dict.keys() and sentiment!=0: # we want upper case to ensure the correct abbrevation of states
                         state_score_dict[state.upper()]+=sentiment
                         state_count_dict[state.upper()]+=1                        
                    else:
                         state_score_dict[state.upper()]=sentiment
                         state_count_dict[state.upper()]=1          
           
            except:
                continue
     
        
    state_sentiment_dict={} #return a dictionary of states and average scores, given a json file###
        
    for state in state_score_dict.keys():
         state_sentiment_dict[state]=float(state_score_dict[state])/state_count_dict[state]
    return state_sentiment_dict
    




def main():
    
     pre_file=sys.argv[1] 
     in_file=sys.argv[2]
   #  pre_file='AFINN-111.txt'
   #  in_file='output.txt'
     pre_dict= predictionary(pre_file)
     state_sentiment_dict=score_file(in_file,pre_dict)
     
     highest_score=None
     happiest_state=None
     
     for state in state_sentiment_dict.keys():
         #print state+" "+str(state_sentiment_dict[state])
         if state_sentiment_dict[state]>highest_score:
             happiest_state=state
             highest_score=state_sentiment_dict[state]
             
     print happiest_state
    
    
    
if __name__=='__main__':
    main()