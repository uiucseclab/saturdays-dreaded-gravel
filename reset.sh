iw dev $1 del
iw phy phy0 interface add $2 type managed
sudo service networking start
sudo service network-manager start
