# got started w/ code from https://dototot.com/how-to-write-a-twitter-bot-with-python-and-tweepy/

import tweepy
import time
import sys
import markovify
import random

CONSUMER_KEY = '2SldYi0UB6lK9eIpLEiLeIcWr'
CONSUMER_SECRET = 'uMJYNDcey4d5I9R7Mi0RRiuVTXe4fF9aoBfQXKIGUpei4WDkfG'
ACCESS_KEY = '908157927407734784-sOu3Na5O4NZ8DIbsD619wvOLmM22VdM'
ACCESS_SECRET = 'mUBmkqDncykEJHBO9egKNpXUZrz8Vnc1gDyxDeiAyySQp'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

BEGIN = "___BEGIN__"

def make_short_sentence_with_start(self, beginning, max_chars, min_chars=0, **kwargs):
        """
        Tries making a sentence that begins with `beginning` string,
        which should be a string of one or two words known to exist in the
        corpus. **kwargs are passed to `self.make_sentence`.
        """
        split = self.word_split(beginning)
        word_count = len(split)
        if word_count == self.state_size:
            init_state = tuple(split)
        elif word_count > 0 and word_count < self.state_size:
            init_state = tuple([ BEGIN ] * (self.state_size - word_count) + split)
        else:
            err_msg = "`make_sentence_with_start` for this model requires a string containing 1 to {0} words. Yours has {1}: {2}".format(self.state_size, word_count, str(split))
            raise ParamError(err_msg)

        return self.make_short_sentence(max_chars)

with open("post_corpora.txt") as f:
    text = f.read()

keywords = open('index.txt').read().splitlines()

text_model = markovify.Text(text, state_size=3)

while(1):
    choice = random.randint(0, 2)

    if choice == 0:
        keyword = random.choice(keywords)
        tweetLength = 138 - len(keyword)
        tweet = keyword.title() + ':\n' + make_short_sentence_with_start(text_model, keyword, tweetLength, min_chars=0)
    else:
        tweet = text_model.make_short_sentence(140)

    api.update_status(tweet)
    # 12 hrs at a time
    time.sleep(43200)
