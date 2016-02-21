import csv

final=[]
rownum1=0
rownum2=0


def mars(id, ilist):
	a = [mark['marks'] for mark in ilist if mark['id']==id]
	return a


with open('test.csv') as ifile:
	reader=csv.reader((line.replace('\0','') for line in ifile))
	for row in reader:
		if rownum1==0:
			rownum1+=1
		else:
			for col in row:
				final.append({'id':row[0],'marks':row[2]})

	print final;

with open('team.csv') as ofile:
	read=csv.reader((line.replace('\0','') for line in ofile))
	for row in read:
		if rownum2==0:
			rownum2+=1
			continue

		t=0
		finalmarks=0
		for col in row:
			t+=1
			b=mars(col[],final)
			print b
			finalmarks += int(b[0])


	print float(finalmarks/t)
	print ",".join(row)










	

