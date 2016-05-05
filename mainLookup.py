#! /usr/bin/python
import json
import sys
import re

# Read data from json files
macInfo = json.load(open('jsonFiles/finalMacs.json'))
credsInfo = json.load(open('jsonFiles/finalCreds.json'))

# Create Mac Address regex
macRegex = re.compile(r'([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}')

# Exit program if argument does not match regex
if len(sys.argv) < 2 or macRegex.search(sys.argv[1]) is None:
    print "Please Enter a Valid MAC address as a command line argument!"
    sys.exit(1)

# Format argument
mac = sys.argv[1][:8].upper()
# Make sure Mac address is in the database
if mac in macInfo:
    # If there are default credentials, print them out
    if macInfo[mac] in credsInfo:
        for cred in credsInfo[macInfo[mac]]:
            print "Username:",cred[0], " Password: ", cred[1]
    # Otherwise, Print out the manufacturer
    else:
        print "We couldn't find any default credentials, but we found a manufacturer!"
        print macInfo[mac]
# If there was no information in the database, notify user
else:
    print "Sorry, we couldn't find any information about that mac address.  Please try again!"
