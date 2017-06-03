from __future__ import print_function
from pushover import init, Client
import os, sys 
from config import *
import urllib
#import threading
import time
import datetime
from time import sleep #just for debugging
#import cups 
import smtplib
# Set default logging handler to avoid "No handler found" warnings.
#import logging
import random
try:  # Python 2.7+
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass
          
#from lxml import html
import requests
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
import re
import json
import urllib2
import socket

type(workers)

totalWorkers = 0
for worker in workers:
	totalWorkers +=1

onlineWorkers = 0
lastWorkers = 0

workerList = {}
downWorkerList = []

##colors
class textcolor:
    INFO = '\033[96m'
    OK = '\033[92m'
    DOWN = '\033[91m'
    WARNING = '\033[93m'
    RESET = '\033[0m'


def workerStats():
	global workerList
	global onlineWorkers
	global lastWorkers
	response = requests.get("https://eiger.alpereum.net/api/stats")
	txt = response.text

	jsonobj = json.loads(txt)
	workerList = {}

	for worker in workers:
		getworker = address + '.' + worker
		workerList[worker] = (jsonobj.get('pools', {}).get('ether').get('workers').get(getworker))

	onlineWorkers = 0
	downWorkerList[:] = []

	for wo in workers:
		if wo in workerList:
			if workerList[wo] == None:
				print (textcolor.DOWN + "Worker: " + wo)
				print ("worker down" + textcolor.RESET)
				print ("")
				downWorkerList.append(wo)

			else:
				print (textcolor.OK + "Worker: " + wo)
				print ("worker alive" + textcolor.RESET)
				print (workerList[wo].get('hashrateString', {}))
				onlineWorkers+= 1
				print ("")
			



def timedelay():
	time.sleep(5)


def sendmail():
	global smtpUser
	global smtpPass
	global toEmail
	global subjectText
	global body

	try:
		fromAdd = smtpUser

		subject = subjectText + str(downWorkerList)
		header = 'To: ' + toEmail + '\n' + 'From: ' + fromAdd + '\n' + 'Subject: ' + subject

		print (header + '\n' + body)

		s = smtplib.SMTP('smtp.gmail.com',587)

		s.ehlo()
		s.starttls()
		s.ehlo()
		s.login(smtpUser,smtpPass)
		s.sendmail(fromAdd,toEmail,header + '\n\n' + body)
		print ("email sent.")

		s.quit()

	except socket.error, exc:
	    print ("Caught exception socket.error : %s" % exc)
	    print ("Please check if port 587 is available.")

def notification():
	global onlineWorkers
	global totalWorkers
	global lastWorkers

	if onlineWorkers < totalWorkers:
		if lastWorkers > onlineWorkers:
			#send mail
			sendmail()
			#send push notification
			init(pushoverToken)
			Client(pushoverUserKey).send_message(str(notificationMessage + str(downWorkerList)), title=notificationTitle)




### Main LOOP ###
while True:
	os.system("clear")
	print (textcolor.INFO + "Checking status......" + textcolor.RESET)
	workerStats()
	#checkworkers()
	notification()
	print ("")
	print ("Total Workers: " + str(totalWorkers))
	print ("Workers Online: " + str(onlineWorkers))
	print ("Last State: " + str(lastWorkers))
	print ("")
	lastWorkers = onlineWorkers
	randomDelay = (random.randint(12,24)*5)
	while (randomDelay > 0):
		sys.stdout.flush()
		print(textcolor.INFO + "- - - REFRESH IN " + str(randomDelay) + " SECONDS" +" - - - " + textcolor.RESET, end='\r')
		randomDelay -= 1
		time.sleep(1)
	sys.stdout.flush()
	print ("")
