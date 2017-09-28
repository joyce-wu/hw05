# Charles Wang and Joyce Wu
# SoftDev1 pd 7
# HW05 -- ... and Now Enjoy Its Contents
# 2017-09-26

from util import occupation
from flask import Flask, render_template
import random

app = Flask(__name__)

# load the table into memory since it doesn't change + easier file changes
jobs = occupation.getJobs("data/occupations.csv")

# Quality of life
@app.route("/")
def index():
    return "<html>Look at occupations <a href='/occupations'>here</a>.</html>"

# Page that has the goods
@app.route("/occupations")
def template():
    return render_template("template.html", title = "Random Job", table = jobs, randJob = occupation.randomJob(jobs))


if __name__ == "__main__":
    app.debug = True
    app.run()
