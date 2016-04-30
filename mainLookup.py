#! /usr/bin/python
import json
import sys
import re

# Read data from json files
macInfo = json.load(open('finalMacs.json'))
credsInfo = json.load(open('finalCreds.json'))

macRegex = re.compile(r'([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}')
if len(sys.argv) < 2 or macRegex.search(sys.argv[1]) is None:
    print "Please Enter a Valid MAC address as a command line argument!"
    sys.exit(1)

mac = sys.argv[1][:8].upper()
if mac in macInfo:
    if macInfo[mac] in credsInfo:
        for cred in credsInfo[macInfo[mac]]:
            print cred[0], cred[1]
    else:
        print "We couldn't find any default credentials, but we found a manufacturer!"
        print macInfo[mac]
else:
    print "Sorry, we couldn't find any information about that mac address.  Please try again!"
