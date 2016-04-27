#! /usr/bin/python
creds = {}
for line in open("default-creds.csv"):
	lineList = line.strip(' \t\r\n').split(',')
	if len(lineList) is not 3:
		continue
	if lineList[0] not in creds:
		creds[lineList[0]] = []
	creds[lineList[0]].append(tuple((lineList[1], lineList[2])))
macs = {}
for line in open("macToManufacturer.csv"):
	lineList = line.strip(' \t\r\n').split(',')
	if len(lineList) is not 2:
		continue
	macs[lineList[0]] = lineList[1]
masterData = {}
for man in creds.keys():
	found = False
	for macman in macs.items():
		if len(macman[1]) < len(man):
			continue
		if man.lower() == macman[1][:len(man)].lower():
			found = True
			if man not in masterData:
				masterData[man] = [[],[]]
			masterData[man][0].append(macman[0])
			continue
	if found:
		masterData[man][1] = creds[man]
for key in masterData.keys():
	if len(masterData[key][0]) > 1:
		print key, masterData[key]
