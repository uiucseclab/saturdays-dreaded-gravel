#! /usr/local/bin/python
import sys
if len(sys.argv) < 2:
	exit(1)
macDict = {}
for line in open('macToManufacturer.csv'):
	pairList = line.strip(' \r\n').split(',')
	if len(pairList) is not 2:
		continue
	macDict[pairList[0]] = pairList[1]
print macDict[sys.argv[1][:8].upper()]
