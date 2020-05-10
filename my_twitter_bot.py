import tweepy
import time
from datetime import datetime
from keys import *
from time import sleep
import os
from os import environ

CONSUMER_KEY = environ['YOUR_CONSUMER_KEY']
CONSUMER_SECRET = environ['YOUR_CONSUMER_SECRET']
ACCESS_KEY = environ['YOUR_ACCESS_KEY']
ACCESS_SECRET = environ['YOUR_ACCESS_SECRET']

def get_days_till_xmas():
	date_format = "%m/%d/"
	now = datetime.now()
	xmas = datetime(now.year, 12, 25)
	delta = xmas - now
	final = delta.days
	if final > 0:
		tweet = str(final) + (" days until christmas! the time is now ") + str(now.hour) + ":" + str(now.minute)
	elif final == 1:
		tweet = "merry christmas eve, one more sleep!"
	elif final == 0:
		tweet = "merry christmas ya filthy animal !!!"
	elif final < 0:
		tweet = "it is past christmas, wait until next year!"
	api.update_status(tweet) 
	return

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


while True:
	print('posting to twitter...')        
	get_days_till_xmas()
	time.sleep(300)
