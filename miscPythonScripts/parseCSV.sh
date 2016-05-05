#! /bin/bash
cat airodumpInfo-01.csv | awk '/^Station MAC/{exit} {print $0}' | tail -n +3 | head -n -3 > temp.csv
echo "Which thing do you want"
cat temp.csv | awk -F',' '{num += 1; print num ": " $14;}' 
read num
line=$(sed "${num}q;d" temp.csv)
bssid=$(echo $line | cut -d ',' -f 1) #$1
echo $bssid
channel=$(echo $line | cut -d ',' -f 4) #$4
echo $channel
encrypt=$(echo $line | cut -d ',' -f 6) #$6
echo $encrypt
