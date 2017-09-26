from flask import Flask, render_template
app = Flask(__name__)

jobList = []
f = open("occupations.csv", "rU")
lines = f.read().splitlines()   ###begin processing of the file into a dictionary
i = 0
while (i < len(lines)):
    line = lines[i].rsplit(",", 1)
    jobList[i] = line
    i += 1



@app.route("/occupations")
def template():
    return app.render_template("template.html", foo = "Random Job", collection = jobList)
