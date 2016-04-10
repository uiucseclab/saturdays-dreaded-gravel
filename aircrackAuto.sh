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
sudo service networking start
sudo service network-manager start
