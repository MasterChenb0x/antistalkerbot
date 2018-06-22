#!/usr/bin/env python
import sys
import os
import re
import random
import  time
import getopt
from datetime import datetime
from twython import Twython


#-- Twitter instance setup
apiKey = 'YOUR_TWITTER_API_KEY'
apiSecret = 'YOUR_TWITTER_API_SECRET'
accessToken = 'YOUR_TWITTER_ACCESS_TOKEN'
accessTokenSecret = 'YOUR_TWITTER_ACCESS_TOKEN_SECRET'

api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)
#--

#-- Functions
def usage():
	"""
	Displays options and examples upon running with bad or missing params
	"""
	print("Usage: antiStalker.py options \n")
	print("	-u/--username,-i/--userid : Username of person potentially being stalked \n")

def getUserInfobyID(userid):
	""" 
	Returns info on user passed to the function as a dictionary object. 
	"""
	# Difference between lookup_user and show_user is list vs dictionary. Not sure on benefits of either yet.
	return api.show_user(user_id=userid)

def getUserInfobyName(username):
	"""
        Returns info on user passed to the function as a dictionary object.
        """
        # Difference between lookup_user and show_user is list vs dictionary. Not sure on benefits of either yet.
        return api.show_user(screen_name=username)

def getFollowersbyName(username):
	"""
	return a list of followers of the username passed as an argument as a dictionary object.
	"""
	return api.get_followers_ids(screen_name=username)

def getFollowersbyID(userid):
        """
        return a list of followers of the username passed as an argument as a dictionary object.
        """
        return api.get_followers_ids(user_id=userid)

def getFriendsbyName(username):
	"""
	return a list of "friends"; people the username follows as a dictionary object.
	"""
	return api.get_friends_ids(screen_name=username)

def getFriendsbyID(userid):
        """
        return a list of "friends"; people the username follows as a dictionary object.
        """
        return api.get_friends_ids(user_id=userid)


#--

# api.update_status(status="Test") 

flist = open("followerlist.txt","r+")
slist = open("suspects.txt","r+")

followerArray = []
suspectsArray = []

#-- Still using the below area for testing until I can put it all together.
result = getUserInfobyID(00000000)
sName = result['screen_name']
print result


followers = getFollowersbyName('target_name')
followerArray = followers['ids']
print followerArray


for fa in followerArray:
	flist.write(str(fa) + "\n")

for i in followerArray:
	print(i)
	try:
		followerDictObj = getFollowersbyID(i)
		suspectsArray = followerDictObj['ids']
		for sa in suspectsArray:
			slist.write(str(sa) + "\n")
	except:
		slist.write(str(i) + " may be a protected account. \n")
		pass
	time.sleep(60)


#for i in followerArray:
#	r = getUserInfobyID(i)
#	nameres = r['screen_name']
#	print "Writing " + nameres + " to file..." "\r\n"
#	flist.write(str(r['id']) + "\n")
#	time.sleep(15)

flist.close()
slist.close()
	
