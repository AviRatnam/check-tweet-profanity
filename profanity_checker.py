# -*- coding: utf-8 -*-

"""
In this code we are checking the degree of profanity for a given tweet.
In this approach, we will see the number of slur words to the total number of words in the tweet. 
Another key aspect we will keep in mind is that not all slurs are equal, some are much worse/ offensive than others. 
Hence, keeping that in mind, we will assign a degree of profanity to each slur as well. 
Hence a tweet such as 'You are sh* t' will be flagged for profanity, but with not as high a score as a tweet like 'You are a f*******' will be marked with a higher score, even though they both have only 1 slur.
"""

import re
import nltk
import json
nltk.download('punkt')

from nltk.tokenize import word_tokenize

#list of slurs assuming slur1 < slur2 .... < slur5 in degree of profanity
slurs = {
         'slur1':0.1,
         'slur2':0.25,
         'slur3':0.5,
         'slur4':0.75,
         'slur5':0.9
         }

#list of tweets

f = open('profanity_tweets.json',)
tweets = json.load(f)

print("List of Tweets: ")
for i in tweets:
  print(i,":",tweets[i])


"""# **Calculating Score**
From a range of 0-1, with 0.0 being a clean sentence and 1 being the worst possible tweet
"""

def match_words(word):
  m_arr=["(.*?)ing$","(.*?)\'s$","(.*?)s$"]
  for k in m_arr:
    m=re.match(k, word)
    if m:
      if m.group(1) in slurs.keys():
          temp = slurs[m.group(1)]
          return temp

  return 0


def tokenise_words(tweet):
  sum=0
  for j in word_tokenize(tweet):
    if j in slurs.keys():
       temp = slurs[j]
       sum+=temp
    else:
       sum+=match_words(j)
  return sum


for i in tweets:
  sum=0
  words=tweets[i].split()
  sum = tokenise_words(tweets[i])

  avg=sum/len(words)
  print(i,":",tweets[i])
  print("Score: ",round(avg,3))
  print("------")