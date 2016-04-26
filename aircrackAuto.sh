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
sudo /bin/bash airodump1.sh $monInterface
airodump-ng -c 6 --bssid 00:0C:E6:A2:01:C0 -w dump $monInterface
sudo service networking start
sudo service network-manager start
