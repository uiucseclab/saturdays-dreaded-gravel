echo "What interface do you want?"
iwconfig 2>/dev/null | grep -o '^[a-z0-9]\+'
read interface
airmon-ng check kill
airmon-ng start $interface
echo "How about now?"
iwconfig 2>/dev/null | grep -o '^[a-z0-9]\+'
read monInterface
echo "We gucci?(y/n)"
read gucci
gnome-terminal -e "sudo /bin/bash -c './airodump1.sh $monInterface; exec /bin/bash -i'"
#echo "Which router are we cracking?"
#print the ESSIDs here, by selecting router we can grab the info we need from CSV and put into the airodump2 command
#read router
gnome-terminal -e "sudo /bin/bash -c './airodump2.sh $monInterface; exec /bin/bash -i'" #will add two more inputs to script for channel and BSSID
echo "Press Enter when done"
read -s
sudo /bin/bash ./reset.sh $monInterface $interface
