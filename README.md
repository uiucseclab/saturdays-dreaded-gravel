# aircrack-auto
> Automated router cracker or whatever

This group of scripts uses aircrack to crack the WEP and WPA/WPA2 passwords of a network as well as interprets the MAC address of the router and will output the default login credentials for a user to use in efforts to login to the router.

## Requirements
- `aircrack` suite
- X-Server

## Instructions - Automated Aircrack
- When running `aircrackAuto.sh`, the script requires user input. To begin, you must specify which network interface you will put into monitor mode. Once that completes, you must select the newly created interface that is in monitor mode to use to capture traffic on the network.
- The script opens a new terminal that shows every router within range and pipes that information into a csv file and parses it. You must then select which router you want to exploit by selecting its corresponding number. The script lists the routers in order of how much network traffic they have, we advise you to select routers at the top of the list.
- The script will then open another terminal that gathers packets and IVs, once it collects enough data the first terminal will present the you with the WPA handshake (assuming WPA/WPA2 was the encryption type, if WEP then the user must gather enough IVs to crack the password). When the handshake gets presented, you can press Enter in the original terminal to begin the password cracking.
- When the cracking is complete or the you wish to abort, press `Enter` in the main terminal. That will reset the interface to your original interface. You must manually close the password cracking window.

## Instructions - Main Lookup
- If this script is given a router MAC address as a command line argument, it will output all the information it has about that address
- First, it will look up the manufacturer based on the first few octets of the MAC address
- Then, it will look up the default login credentials for that router manufacturer
- Depending on what information is in the database, the script will either print out no results, a manufacturer, or all the default credentials that are publicly available

## Instructions - Generating MAC Address Database
- Run the following python scripts in the correct order
    - `python miscPythonScripts/default-pass.py --reload` This script fetches a list of router manufacturers from an online database as well as the default credentials for those manufacturers. The script combines all the information into a simple csv file and saves the result in the csvFiles directory.
    - `cd miscPythonScripts && python combineInfo.py` This script combines the default credential information from the previous script with the manufacturer to MAC address mapping csv file. This effectively gives a MAC address to default credential mapping.


## Credits
- http://www.routerpasswords.com/
- http://www.aircrack-ng.org/

## Areas for Expansion
- One idea we had was to cause every user on the network to deauthorize. This would force all users to re-autherize to the network, which would result in a much shorter time required to find the WPA handshake or WEP IVs. In order to force users on the network to deauthorize, we would send dissasociate packets to them. In the end, we decided to not implement this for this project due to legality concerns.
- Another idea for the future would be automating even more of the router-hacking process. Namely, once a network password has been cracked, automatically try all the default credentials to gain access to the router config page. If the default credentials didn't work, the script could also try exploiting common router vulnerabilities to gain access. We could also automate different processes, such as sitting on a network and monitoring traffic or automatically ARP spoofing.

