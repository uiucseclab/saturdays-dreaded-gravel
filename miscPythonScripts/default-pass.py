from bs4 import BeautifulSoup
import urllib
import urllib2
import sys

print sys.argv

creds = {};
credfile = open('./default-creds.csv', 'r+')

# Print the help text
if '--help' in sys.argv:
    print 'Usage: python default-pass.py [Manufacturer]...'

# Reload the credential file
if '--reload' in sys.argv:

    # Get list of router manufacturers
    manufct_list_source = urllib.urlopen('http://www.routerpasswords.com').read()
    manufct_list_soup = BeautifulSoup(manufct_list_source, "html.parser")
    for child in manufct_list_soup.find_all('select')[0].contents:
        if child.name == 'option':
            value = child['value']
            if value not in creds:
                creds[value] = []

    print('Found %d manufacturers' % len(creds))

    # Loop through each manufacturer and collect all username/password combinations
    count = 0
    for manufct in creds:
        credfile.write('%s\n' % manufct)
        count += 1;
        print('Scanning %d / %d: %s' % (count, len(creds), manufct) )

        form_data = {'findpass': 1, 'router': manufct, 'findpassword': 'Find Password'}
        data = urllib.urlencode(form_data)
        cred_list_req = urllib2.Request('http://www.routerpasswords.com', data)
        cred_list_source = urllib2.urlopen(cred_list_req).read()
        cred_list_soup = BeautifulSoup(cred_list_source, "html.parser")

        # Loop through table results and store username/password combinations
        for row in cred_list_soup.find_all('tr'):
            if len(row.find_all('td')) == 5:
                username = row.find_all('td')[3].string
                password = row.find_all('td')[4].string
                if (username, password) not in creds[manufct]:
                    creds[manufct].append((username, password))
                    credfile.write('%s,%s,%s\n' % (manufct, username, password))
                    credfile.flush()

# Return to the beginning of the file
credfile.seek(0)

# Clear the credential file if the user requests it
if '--clear' in sys.argv:
    credfile.truncate()
else:
    if credfile.readline() == '':
        print 'EMPTY! You should probably run with `--reload`'
    else:
        for query in sys.argv:
            if query != 'default-pass.py' and query != '--clear' and query != '--reload' and query != '--help':
                print query


# Close the credential file
credfile.close()

