from bs4 import BeautifulSoup
import urllib.request as url
import urllib.parse

creds = {};

# Get list of router manufacturers
manufct_list_source = url.urlopen('http://www.routerpasswords.com').read()
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
    count += 1;
    print('Scanning %d / %d: %s' % (count, len(creds), manufct) )

    form_data = {'findpass': 1, 'router': manufct, 'findpassword': 'Find Password'}
    cred_list_request = url.Request('http://www.routerpasswords.com',
            urllib.parse.urlencode(form_data).encode('ascii'))
    cred_list_source = url.urlopen(cred_list_request).read()
    cred_list_soup = BeautifulSoup(cred_list_source, "html.parser")

    # Loop through table results and store username/password combinations
    for row in cred_list_soup.find_all('tr'):
        if len(row.find_all('td')) == 5:
            username = row.find_all('td')[3].string
            password = row.find_all('td')[4].string
            if (username, password) not in creds[manufct]:
                creds[manufct].append((username, password))

print(creds)

#TODO: Print to file or some shit
