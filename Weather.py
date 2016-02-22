import urllib2
import re
import json



city=str(raw_input("Enter The Name of the City :  "))

response = urllib2.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=4a87519db6e540f39c6651e9e9f89a8b')
data= json.load(response)
print "Your City : " + city
print "Current Weather : "+ str(data['main']['temp']-273)+ "C"
