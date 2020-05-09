import tweepy
from datetime import datetime
from keys import *
from time import sleep


#print('this is my christmas countdown twitter bot')

INTERVAL = 15  # tweet every 6 hours

def get_days_till_xmas():
	date_format = "%m/%d/"
	now = datetime.now()
	xmas = datetime(now.year, 12, 25)
	delta = xmas - now
	final = delta.days
	if final > 0:
		tweet = str(final) + (" days until christmas!")
	elif final == 1:
		tweet = "merry christmas eve, one more sleep!"
	elif final == 0:
		tweet = "merry christmas ya filthy animal !!!"
	elif final < 0:
		tweet = "it is past christmas, wait until next year!"
	print tweet 
	return tweet

def send_tweet():
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
	api = tweepy.API(auth)
	while True:
		print('posting to twitter...')        
		tweet = get_days_till_xmas()
		api.update_status(tweet)
		time.sleep(INTERVAL)

send_tweet()