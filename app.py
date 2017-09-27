# Charles Wang and Joyce Wu
# SoftDev1 pd 7
# HW05 -- ... and Now Enjoy Its Contents
# 2017-09-26

from flask import Flask, render_template
from decimal import Decimal
import random

app = Flask(__name__)

#creates a list of lists with two values to pass to HTML template for table generation
#the first place stores the job name; the second the percentage
#maintains original order of list w/o dictionary
jobList = []
f = open("occupations.csv", "rU")
lines = f.read().splitlines()
i = 0
while (i < len(lines)):
    #split each line read by the first rightmost comma (some job names have commas in them)
    line = lines[i].rsplit(",", 1)
    jobList.append(line)
    i += 1


'''
#Get a random job
ramdom = random.randrange(len(jobList) - 1)
i = 1
while (ramdom > 0):
    ramdom -= float(jobList[i][1])
    i += 1
job = jobList[i]

@app.route("/occupations")
def template():
    return app.render_template("template.html", foo = "Random Job", collection = jobList, randJob = job)

#quality of life
@app.route('/')
def hello():
	return "<a href= '/occupations'>go here</a>."

if __name__ == '__main__':
'''

#use our last hw to get a random job
myList = []
    #goes through each list, multiplying each percentage by 10
for job in jobList:
    if not (job[0] == "Job Class" or job[0] == "Total"):
        val = Decimal(job[1]) * 10
        for x in range(val):
            myList.append(job[0]) #adds occupation by value
job = random.choice(myList) #randomly chooses occupation from list

@app.route("/")
def index():
    return "<html>Look at occupations <a href='/occupations'>here</a>.</html>"

@app.route("/occupations")
def template():
    return render_template("template.html", foo = "Random Job", collection = jobList, randJob = job)

if __name__ == "__main__":
    app.debug = True
    app.run()
