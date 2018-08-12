#!/usr/bin/env python
import sys
import os
import re
import random
import time
from datetime import datetime
from twitfunctions import *
from twython import Twython

#--
# AntiStalkerBot by MasterChen, @chenb0x 2018.
# Donations are welcome via Paypal, chenb0xllc[at]gmail.com
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

if __name__ == "__main__":
	try:
		start(sys.argv[1:])
	except KeyboardInterrupt:
		print("Program stopped by user.")
	except:
		usage()	

