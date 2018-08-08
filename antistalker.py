#!/usr/bin/env python
import sys
import os
import re
import random
import time
from datetime import datetime
#from twitfunctions import *
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
	print("Usage: ./antiStalker.py TwitterID|TwitterUsername \n")
	print("		TwitterID or TwitterUsername will usually be your own if you are monitoring your own acccount for stalker activity. \n")
	print("		 \n")
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
	twitName = ""
	twitID = ""
	flist = open("followerlist.txt","w+")
	slist = open("suspects.txt","w+")
	followerArray = []
	suspectsArray = []
	if len(sys.argv) < 1:
		usage()
	if sys.argv[1].isdigit() == True:
		twitID = str(sys.argv[1])
		result = getUserInfobyID(twitID)
                followers = getFollowersbyID(twitID)
                followerArray = followers['ids']
                # Write followers to file for later analysis
                for fa in followerArray:
                        flist.write(str(fa) + "\n")
                # Build suspect list
                for i in followerArray:
                        print("Retrieving " + str(i) + "\'s followers")
                        try:
                                followerDictObj = getFollowersbyID(i)
                                suspectArray = followerDictObj['ids']
                                for sa in suspectArray:
                                        slist.write(str(sa) + "\n")
                        except:
                                slist.write(str(i) + " may be a protected account. \n")
                                pass
                        time.sleep(60)  # should avoid rate limit
	else:
		twitName = str(sys.argv[1])
		result = getUserInfobyName(twitName)
		followers = getFollowersbyName(twitName)
		followerArray = followers['ids']
		# Write followers to file for later analysis.
		for fa in followerArray:
			flist.write(str(fa) + "\n")
		# Build suspect list
		for i in followerArray:
			print("Retrieving " + str(i) + "\'s followers")
			try:
				followerDictObj = getFollowersbyID(i)
				suspectArray = followerDictObj['ids']
				for sa in suspectArray:
					slist.write(str(sa) + "\n")
			except:
				slist.write(str(i) + " may be a protected account. \n")
				#pass
			time.sleep(60) # should avoid rate limit. 

	flist.close()
	slist.close()
	sys.exit()

#--

'''
#-- Still using the below area for testing until I can put it all together.



'''
if __name__ == "__main__":
	try:
		start(sys.argv[1:])
	except KeyboardInterrupt:
		print("Program stopped by user.")
	except:
		usage()	

