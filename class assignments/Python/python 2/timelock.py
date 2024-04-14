#########################################################
#Name: Joshua Brack					#
#Date: 5/8/2020						#
#Python Ver- 2.7					#
#Program Name: Timelock					#
#Desc: Calculate elapsed time in seconds from some 	#
#	arbitrary epoch, then hash it twice with md5	#
# 	then get first two letters from left to right 	#
# 	and first two numbers from right to left to use #
# 	as code						#
#########################################################

from sys import stdin
from datetime import datetime
import pytz
from hashlib import md5

# debug mode
DEBUG = False

# set to True if on the challenge server
ON_SERVER = False

# valid time interval
INTERVAL = 60

# manual current datetime?
MANUAL_DATETIME = "2017 04 23 18 02 30"


# get epoch time
epoch = stdin.read().rstrip("\n")

#setup settings to convert epoch from central to UTC
local = pytz.timezone ("Us/Central")
naive = datetime.strptime (epoch, "%Y %m %d %H %M %S")
local_dt = local.localize(naive, is_dst=None)
epoch = local_dt.astimezone(pytz.utc)

#get current time (as utc) if MANUAL_DATETIME is empty
if (len(MANUAL_DATETIME) ==0):
	current= datetime.utcnow()
	current = pytz.UTC.localize(current)
	current.strftime("%Y-%m-%d %H:%M:%S")
else:
	naive = datetime.strptime (MANUAL_DATETIME, "%Y %m %d %H %M %S")
	local_dt = local.localize(naive, is_dst=None)
	current = local_dt.astimezone(pytz.utc)

# format epoch and current as needed
epoch.strftime ("%Y-%m-%d %H:%M:%S")
current.strftime("%Y-%m-%d %H:%M:%S")

if (DEBUG):
        print "Epoch (UTC): {}".format(epoch)
        print "Current (UTC): {}".format(current)

#Calculate amount of seconds that have elapsed between the two times
duration = current-epoch
duration = duration.total_seconds()
#adjust duration to be seconds that start a 60 second interval (or whatever INTERVAL is)
startSeconds = int(duration/INTERVAL)*60
if(DEBUG):
	print "Seconds: {}".format(duration)
	print "Seconds: {}".format(startSeconds)

#Get an MD5 hash (twice) of the amount of time that elapsed between the two
md5Hash = md5(md5(str(startSeconds)).hexdigest())
md5Hash = md5Hash.hexdigest()

if(DEBUG):
	print "Hash is {}".format(md5Hash)

#get the first two letters from left to right and the last 2 numbers from right to left as your code
#harvest letters
code = ""
for char in md5Hash:
	#if not a digit
	if(not char.isdigit()):
		code += char
	if(len(code)==2):
		break
#harvest numbers from right to left
for char in reversed(md5Hash):
	#if a digit
	if(char.isdigit()):
		code+=char
	if(len(code)==4):
		break
#print out your code
print code

