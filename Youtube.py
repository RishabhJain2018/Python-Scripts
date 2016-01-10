import pafy

url= raw_input("Enter your url")
video=pafy.new(url)
print "Do you Want to Download it or want to extract information ?"
choice = raw_input("Input d to Download or ei to Extract Information")

if choice == 'd':
	best=video.getbest()
	best.download(quiet=False)
elif choice == 'ei':
	print "Title : " +video.Title
	print "Rating : " +str(video.rating) 
	print "View Count : " + str(video.viewcount) + "Author : " + video.author + "Length :" + sstr(video.length)
	print "Duration :" + str(video.duration) + "Likes : "+ str(video.likes) + "Dislikes : "+ str(video.dislikes)
	print "Description : "+ video.description
	print "Published on Date : " + str(video.published)
else:
	print "Oops wrong Choice !"
