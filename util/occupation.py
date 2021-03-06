# Charles Wang and Joyce Wu
# SoftDev1 pd 7
# HW05 -- ... and Now Enjoy Its Contents
# 2017-09-26

import random

# returns a list of lists with two values
## the first place stores the job name; the second the percentage
## maintains original order of list w/o dictionary
## includes header + total
def getJobs(fileName):
    jobList = []
    f = open(fileName, "rU")
    lines = f.read().splitlines()
    i = 0
    while (i < len(lines)):
        #split each line read by the first rightmost comma (some job names have commas in them)
        line = lines[i].rsplit(",", 1)
        jobList.append(line)
        i += 1
    return jobList

# use our last hw to get a random job
''' brute force random occupation
def randomJob():
    myList = []
    #goes through each list, multiplying each percentage by 10
    for job in jobList:
        if not (job[0] == "Job Class" or job[0] == "Total"):
            val = Decimal(job[1]) * 10
            for x in range(val):
                myList.append(job[0]) #adds occupation by value
    job = random.choice(myList) #randomly chooses occupation from list
'''

# less memory intensive way
def randomJob(jobList):
    ramdom = random.randrange(len(jobList) - 1)
    i = 1
    while (ramdom > 0):
        ramdom -= float(jobList[i][1])
        i += 1
    return jobList[i][0] + ", " + jobList[i][1]
