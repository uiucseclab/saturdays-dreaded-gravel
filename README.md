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

## Instructions - Default Credentials
- Run the following python scripts in the correct order
    - `python miscPythonScripts/default-pass.py --reload` This script fetches a list of router manufacturers from an online database as well as the default credentials for those manufacturers. The script combines all the information into a simple csv file and saves the result in the csvFiles directory.
    - ???
    - Profit

## Credits
- http://www.routerpasswords.com/
- http://www.aircrack-ng.org/

# Areas for Expansion
- Talk about deauth here
- Talk about auto form entering here

