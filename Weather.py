import urllib2
import re
import json
from urllib2 import urlopen

def getPublicIP():
	data= str(urlopen('http//checkip.dyndns.com/').read())
	return re.compile(r'Address : (\d+.\d+.\d+.\d+)').search(data).group(1)

IP=str(getPublicIP)

url = 'http://info.io/' + IP + '/json'
response=urlopen(url)
data=json.load(response)
city=data['city']

response = urllib2.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city)
data= json.load(response)
print "Your City : " + city
print "Current Weather : "+ str(data['main']['temp']-273)+ "C"
