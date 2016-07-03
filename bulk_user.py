# Generates Users from user_start to (user_end-1)

user_start=int(raw_input())
user_end = int(raw_input())
branch=raw_input()
users = ["%.3d" % users for users in range(user_start, user_end)]
for user in users:
	print "user_id is "+"16/"+ branch + "/"+ str(user)
	print "password is "+"16/"+ branch + "/"+ str(user)
