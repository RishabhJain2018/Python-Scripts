import urllib2
import urllib
import csv
from random import randrange
import random

domain=['gmail', 'yahoo', 'hotmail', 'rediffmail']

with open('final.csv', 'rb') as csvfile:

	for line in csvfile.readlines():
		names = line.split(',')
		

for i in range(0,100):
	a=str(randrange(7,10))
	b=str(randrange(7,10))
	c=str(randrange(70,100))
	d=str(randrange(111111, 999999))

	name = names[i]
	phone_no = a+b+c+d	
	email = names[i].lower()+str(randrange(1, 9999))+"@"+random.choice(domain)+".com"
	values = {'name': name, 'email':email, 'phone_no':phone_no}

	try:
		url = "http://www.jbitdoon.com/index.php"
		data = urllib.urlencode(values)
		req = urllib2.Request(url, data)
		response= urllib2.urlopen(req)
		print "i : ",response.getcode()

	except urllib2.HTTPError as e:
		if e.code == 404:
			print "Error 404"
		else:
			body=response.read()
			print body
