#! /usr/bin/python
import sys
if len(sys.argv) < 2:
	exit(1)
manList = []
macDict = {}
for line in open('macToManufacturer.csv'):
	pairList = line.strip(' \r\n').split(',')
	if len(pairList) is not 2:
		continue
	manList.append(pairList[1])
	macDict[pairList[0]] = pairList[1]
setList = set(manList)
for item in setList:
	print item
#print macDict[sys.argv[1][:8].upper()]
