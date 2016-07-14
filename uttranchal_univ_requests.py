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
	mobile = a+b+c+d	
	email = names[i].lower()+str(randrange(1, 9999))+"@"+random.choice(domain)+".com"
	state = ['Andaman and Nicobar','Andhra Pradesh','Arunachal Pradesh', 'Assam', 'Bihar', 'Chandigarh','Chhattisgarh','Dadra and Nagar Haveli', 'Daman and Diu', 'Delhi', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jammu and Kashmir', 'Jharkhand','Karnataka', 'Kerala', 'Lakshadweep', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Pondicherry', 'Punjab','Rajasthan','Sikkim']
	course = ['Polytechnic (Diploma) - Mechanical Engineering', 'Polytechnic (Diploma) - Civil Engineering', 'Polytechnic (Diploma) - Electrical Engineering', 'Polytechnic (Diploma) Lateral Entry - Mechanical Engineering', 'Polytechnic (Diploma) Lateral Entry - Civil Engineering', 'Polytechnic (Diploma) Lateral Entry - Civil Engineering', 'Polytechnic (Diploma) Lateral Entry - Electrical Engineering', 'B.Tech - Electronics and Communication Engineering', 'B.Tech - Computer Science and Engineering', 'B.Tech - Information Technology', 'B.Tech - Mechanical Engineering', 'B.Tech - Electrical Engineering', 'B.Tech - Civil Engineering', 'B.Tech - Petroleum Engineering', 'B.Tech (Lateral Entry) - Electronics and Communication Engineering', 'B.Tech (Lateral Entry) - Computer Science and Engineering', 'B.Tech (Lateral Entry) - Mechanical Engineering', 'B.Tech (Lateral Entry) - Electrical Engineering','B.Tech (Lateral Entry) - Civil Engineering','B.Tech (Lateral Entry) - Petroleum Engineering','B.Sc. Agriculture', 'B.Sc. Forestry','B.Sc. Biotechnology (Hons.)','B.Sc. Food Technology (Hons.)', 'B.Sc. Physics (Hons.)', 'B.Sc. Chemistry (Hons.)', 'B.Sc. Mathematics (Hons.)', 'M.Tech - CSE', 'M.Tech - CSE (Info. Secu. and  Mgt.)', 'M.Tech - CSE (Dist. Comp.)', 'M.Tech - ECE (Adv. Comp. Engg.)', 'M.Tech - ME (Thm. Engg.)', 'M.Tech - CE (Env. Engg.)', 'M.Tech - CE (Stru. Engg.)', 'M.Tech - Petroleum Technology', 'M.Sc (Industrial Chemistry)','Ph.D. in CSE', 'Ph.D. in ECE', 'Ph.D. in Civil Engg.', 'Ph.D. in Physics', 'Ph.D. in Chemistry', 'Ph.D. in Mathematics', 'Ph.D. in English', 'Ph.D. in Economics', 'BBA', 'BCA', 'B.Sc (IT)', 'B.Com. (Hons.)', 'MBA', 'Corporate - MBA', 'MCA (Leteral Entry)', 'Ph.D. in Management', 'BALLB (Hons)', 'BBA LLB (Hons)', 'LLB (Hons)', 'LLM - 1 Year', 'Ph.D. in Law', 'D.Pharm', 'B.Pharm', 'Ph.D. in Pharmacy']	
	# state = ['B Tech(CSE)','B Tech(IT)','B Tech(ME)','B Tech(CIVIL)','B Tech(EEE)','B Tech(ECE)','B Pharm','BBA','BBA(HM)','BCA','B.Sc(IT)','B.Sc(Agriculture)','B.Sc(Forestry)','B.Com','BSC(PCM)','BSC(CBZ)','BSC(Horti)','MCA','M Tech(CSE)','M Tech(ME)','M Tech(EEE)','M Tech(ECE)','D.Pharam','Diploma(CS)','Diploma(EE)','Diploma(EC)','Diploma(ME)']
	
	values = {'name': name, 'mobile': mobile, 'email':email, 'state': random.choice(state), 'course': random.choice(str(course))}

	try:
		url = "https://uttaranchaluniversity.ac.in/apply/forms/horizon1.php"
		data = urllib.urlencode(values)
		request = urllib2.Request(url, data)
		response = urllib2.urlopen(request)
		print str(i)+" : ",response.getcode()
		# print response.read()

	except urllib2.HTTPError as e:
		if e.code == 404:
			print "Error 404"
		else:
			body=response.read()
			print body
