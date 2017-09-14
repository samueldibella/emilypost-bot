# got started w/ code from https://dototot.com/how-to-write-a-twitter-bot-with-python-and-tweepy/
# !/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy
import time
import sys
import markovify

#argfile = str(sys.argv[1])

# enter the corresponding information from your Twitter application:
CONSUMER_KEY = '2SldYi0UB6lK9eIpLEiLeIcWr'  # keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'uMJYNDcey4d5I9R7Mi0RRiuVTXe4fF9aoBfQXKIGUpei4WDkfG'  # keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '908157927407734784-sOu3Na5O4NZ8DIbsD619wvOLmM22VdM'  # keep the quotes, replace this with your access token
ACCESS_SECRET = 'mUBmkqDncykEJHBO9egKNpXUZrz8Vnc1gDyxDeiAyySQp'  # keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

with open("post_corpora.txt") as f:
    text = f.read()

text_model = markovify.Text(text, state_size=3)

while(1):
    api.update_status(text_model.make_short_sentence(140))
    time.sleep(1800)

#for i in range(5):
    #print()


#filename = open(argfile,'r')
#f = filename.readlines()
#filename.close()

#for line in f:
#    api.update_status(line)
#     #  Tweet every 15 minutes
