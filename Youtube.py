import pafy

url= raw_input("Enter your url")
video=pafy.new(url)
print "Do you Want to Download it or want to extract information ?"
choice = raw_input("Input d to Download or ei to Extract Information")

if choice == 'd':
	best=video.getbest()
	best.download(quiet=False)