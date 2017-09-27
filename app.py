#Charles Weng and Joyce Wu
#P7 SoftDev
#HW05 ... And Now Enjoy Its Contents
#9/27/18

import  random
from flask import Flask, render_template
app = Flask(__name__)

#creates a list of lists with two values to pass to HTML template for table generation
#the first place stores the job name; the second the percentage
jobList = []
f = open("occupations.csv", "rU")
lines = f.read().splitlines()
i = 0
while (i < len(lines)):
    #split each line read by the first rightmost comma (some job names have commas in them)
    line = lines[i].rsplit(",", 1)
    jobList.append(line)
    i += 1

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
    app.debug = True
    app.run()
