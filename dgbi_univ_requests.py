import urllib2
import urllib
import csv
from random import randrange
import random

domain=['gmail', 'yahoo', 'hotmail', 'rediffmail']

with open('names.csv', 'rb') as csvfile:

	for line in csvfile.readlines():
		names = line.split(',')
		

for i in range(0,100):
	a=str(randrange(7,10))
	b=str(randrange(7,10))
	c=str(randrange(70,100))
	d=str(randrange(111111, 999999))

	name = names[i]
	contact = a+b+c+d	
	email = names[i].lower()+str(randrange(1, 9999))+"@"+random.choice(domain)+".com"
	courses = ['B Tech(CSE)','B Tech(IT)','B Tech(ME)','B Tech(CIVIL)','B Tech(EEE)','B Tech(ECE)','B Pharm','BBA','BBA(HM)','BCA','B.Sc(IT)','B.Sc(Agriculture)','B.Sc(Forestry)','B.Com','BSC(PCM)','BSC(CBZ)','BSC(Horti)','MCA','M Tech(CSE)','M Tech(ME)','M Tech(EEE)','M Tech(ECE)','D.Pharam','Diploma(CS)','Diploma(EE)','Diploma(EC)','Diploma(ME)']
	query = ['How to apply?', 'What is the last date to apply?', 'please call & explain the things.']
	
	values = {'name': name, 'contact': contact, 'email':email, 'courses':random.choice(courses), 'query':random.choice(str(query))}

	try:
		url = "http://www.dbgidoon.ac.in/registration-form/submit1.php"
		data = urllib.urlencode(values)
		request = urllib2.Request(url, data)
		response = urllib2.urlopen(request)
		print str(i)+" : ",response.getcode()
		#print response.read()

	except urllib2.HTTPError as e:
		if e.code == 404:
			print "Error 404"
		else:
			body=response.read()
			print body
