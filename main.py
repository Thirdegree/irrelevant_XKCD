import praw, re, random
from time import sleep, time
from collections import deque

r = praw.Reddit("Irrelevant_XKCD by /u/Thirdegree")

def login_():
	USERNAME = raw_input("Username?\n> ")
	PASSWORD = raw_input("Password?\n> ")
	r.login(USERNAME, PASSWORD)

done = deque(maxlen=300)

Trying = True
while Trying:
	try:
		login_()
		Trying = False
	except praw.errors.InvalidUserPass:
		print "Invalid Username/password, please try again."

def is_xkcd(post):
	in_post = re.search("(?i)((\[)*relevant(\])*(\[)*XKCD(\])*)", post.body)
	if in_post:
		post.reply("[Irrelevant XKCD](xkcd.com/%d"%random.randint(1,int(time())/60/60/25-14746))
