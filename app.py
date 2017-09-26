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
    jobList[i] = line
    i += 1

job =

@app.route("/occupations")
def template():
    return app.render_template("template.html", foo = "Random Job", collection = jobList, randJob)
