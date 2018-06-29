#!/usr/bin/env python
import sys
import os
import re
import random
import time
import getopt
from datetime import datetime
from twython import Twython


#-- Twitter instance setup
apiKey = 'YOUR_API_KEY'
apiSecret = 'YOUR_API_SECRET'
accessToken = 'YOUR_ACCESS_TOKEN'
accessTokenSecret = 'YOUR_ACCESS_TOKEN_SECRET'

api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)
#--

#-- Functions
def usage():
	"""
	Displays options and examples upon running with bad or missing params
	"""
	print("Usage: ./antiStalker.py options \n")
	print("		-u : Twitter handle of Stalker's Target...probably your own handle \n")
	print("		-i : Same as -u but with ID instead of handle \n")
	sys.exit()

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

def start(argv):
	if len(sys.argv) < 1:
		usage()
		sys.exit()
	try:
		opts, args = getopt.getopt(argv, "u:i")
	except getopt.GetoptError:
		usage()
		sys.exit()
	except Exception, e:
		pass
	twitName = ""
	twitID = ""
	flist = open("followerlist.txt","r+")
	slist = open("suspects.txt","r+")
	followerArray = []
	suspectsArray = []
	for opt, arg in opts:
		if opt == '-u':
			twitName = str(arg)
		elif opt == '-i':
			twitID = int(arg)			
	if twitName != "":
		result = getUserInfobyName(twitName)
		print(result)
	elif twitID != "":
		result = getUserInfobyID(twitID)
		print(result)
	flist.close()
	slist.close()
	sys.exit()

#--

'''
#-- Still using the below area for testing until I can put it all together.
result = getUserInfobyID(00000000)
sName = result['screen_name']
print sName


followers = getFollowersbyName('target')
followerArray = followers['ids']
print followerArray

# Write followers to file for later analysis.
for fa in followerArray:
	flist.write(str(fa) + "\n")

# Grab followers of followers to build a list of potential suspects.
for i in followerArray:
	print("Retrieving " + str(i) + "\'s followers")
	try:
		followerDictObj = getFollowersbyID(i)
		suspectsArray = followerDictObj['ids']
		for sa in suspectsArray:
			slist.write(str(sa) + "\n")
	except: # private accounts. This may still have potential
		slist.write(str(i) + " may be a protected account. \n")
		pass
	time.sleep(30) # should avoid rate limit


flist.close()
slist.close()

'''
if __name__ == "__main__":
	try:
		start(sys.argv[1:])
	except KeyboardInterrupt:
		print("Program stopped by user.")
	except:
		sys.exit()	

