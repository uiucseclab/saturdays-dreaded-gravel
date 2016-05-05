#! /usr/bin/python
import json
# Parse default credentials CSV
# Create mapping of Manufacturer to list of
# uname password tuples
creds = {}
for line in open("../csvFiles/default-creds.csv"):
    lineList = line.strip(' \t\r\n').split(',')
    if len(lineList) is not 3:
        continue
    if lineList[0] not in creds:
        creds[lineList[0]] = []
    creds[lineList[0]].append(tuple((lineList[1], lineList[2])))
# Parse Mac address to manufacturer CSV
# Create Mapping of Macs to Manufacturer
macs = {}
for line in open("../csvFiles/macToManufacturer.csv"):
    lineList = line.strip(' \t\r\n').split(',')
    if len(lineList) is not 2:
        continue
    macs[lineList[0]] = lineList[1]
# Consolodate two lists into one by finding commonalities in manufacurer names
masterData = {}
for man in creds.keys():
    found = False
    for macman in macs.iteritems():
        if len(macman[1]) < len(man):
            continue
        if man.lower() == macman[1][:len(man)].lower():
            found = True
            if man not in masterData:
                masterData[man] = [[],[]]
                masterData[man][0].append(macman[0])
                macs[macman[0]] = man
                continue
    if found:
        masterData[man][1] = creds[man]
json.dump(macs,open('../jsonFiles/finalMacs1.json', 'w'))
json.dump(creds,open('../jsonFiles/finalCreds1.json', 'w'))
json.dump(masterData,open('../jsonFiles/combined1.json', 'w'))
