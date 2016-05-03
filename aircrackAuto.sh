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
x-terminal-emulator -e "sudo /bin/bash -c './airodump1.sh $monInterface; exec /bin/bash -i'"
#echo "Which router are we cracking?"
#print the ESSIDs here, by selecting router we can grab the info we need from CSV and put into the airodump2 command
#read router
cat airodumpInfo-01.csv | awk '/^Station MAC/{exit} {print $0}' | tail -n +3 | head -n -3 > temp.csv
echo "Which thing do you want"
cat temp.csv | awk -F',' '{num += 1; print num ": " $14;}' 
read num
line=$(sed "${num}q;d" temp.csv)
bssid=$(echo $line | cut -d ',' -f 1) #$1
channel=$(echo $line | cut -d ',' -f 4) #$4
encrypt=$(echo $line | cut -d ',' -f 6) #$6
x-terminal-emulator -e "sudo /bin/bash -c './airodump2.sh $monInterface $bssid $channel; exec /bin/bash -i'" #will add two more inputs to script for channel and BSSID
echo "Press Enter when done"
read -s
sudo /bin/bash ./reset.sh $monInterface $interface
