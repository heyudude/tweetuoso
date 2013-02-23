#!/usr/bin/env python
# -*- coding: utf-8 -*-

__appname__ = 'api_rate_limit'
__version__ = "0.2"
__author__ = "@c0ding <https://twitter.com/c0ding>"
__licence__ = "WTFPL"

import tweepy as tw

consumer_key = ''
consumer_secret = ''
access_token = '' 
access_secret = ''

def rate_limit():
	try:
		auth = tw.OAuthHandler(consumer_key, consumer_secret)
		auth.set_access_token(access_token, access_secret)
		api = tw.API(auth)
		print api.rate_limit_status()
		
	except tw.TweepError:
		print "Error occured, failed to get token"
		return
					
if __name__ == '__main__':
	rate_limit()