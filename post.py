#
# !/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy
import time
import sys

argfile = str(sys.argv[1])

# enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'CaFBr0sdmwQygto4GwrJd2Tye'  # keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'ovfxLDdKSAxINAZFcW7oqM0F3nbq44Yn6UI8tBFrlbAzoaa43D'  # keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '1420942116-tAuqCQ5q108QiDeEfZA7SKw9LN6W8jysqlM7QAT'  # keep the quotes, replace this with your access token
ACCESS_SECRET = '4E7LNGwwwnq7HEHk9fyA6TH47JnbjTgCSkKXKyB3enHZy'  # keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename = open(argfile,'r')
f = filename.readlines()
filename.close()

for line in f:
    api.update_status(line)
    time.sleep(1800) #  Tweet every 15 minutes
