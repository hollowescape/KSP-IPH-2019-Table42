from flask import Flask 
from FB.src import *

app = Flask(__name__)


Overview = [] #
work = []	#
hometown = [] #
family = []		#
friends = []	#
basicinfo = [] #
cplace = []   #
images = []  #

import os

fo = open("Overview.txt", "rw+")
line = fo.readlines()
for i in line:
	Overview.append(i)
fo.close()	


fo = open("Work and Education.txt", "rw+")
line = fo.readlines()
for i in line:
	work.append(i)
fo.close()	


fo = open("Contact and Basic Info.txt", "rw+")
line = fo.readlines()
for i in line:
	basicinfo.append(i)

basicinfo = basicinfo[3:]
for i in range(10):
	if(i%2!=0):
		basicinfo[i/2] = { basicinfo[i-1]:basicinfo[i]}
basicinfo = basicinfo[0:5]
fo.close()	


fo = open("Family and Relationships.txt", "rw+")
line = fo.readlines()
for i in line:
	family.append(i)
family = family[4:-1]
for i in range(len(family)):
	family[i] = (family[i].split(" "))
fo.close()	

fo = open("Mutual Friends.txt", "rw+")
line = fo.readlines()
for i in line:
	friends.append(i.split(",")[1])
fo.close()	

fo = open("Places Lived.txt", "rw+")
line = fo.readlines()
cplace.append({line[0]:line[1]})
fo.close()	

os.chdir(os.getcwd()+"/Uploaded Photos")
images = os.listdir(os.getcwd())


obj = [
	{"Overview":Overview},
	{"Work": work},
	{"Hometown":hometown},
	{"Family":family},
	{"Friends":friends},
	{"Basicinfo": basicinfo},
	{"Current Place":cplace},
	{"Image-url":images}
]


@app.route("/facebook")
def fb():
	return {"Data": obj}

app.run()
