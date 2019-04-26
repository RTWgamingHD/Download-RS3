#!/bin/bash

echo "[*] Attempting to install RuneScape-NXT. Please wait ..."
sleep 5s
clear

sudo -s -- << EOF
wget -O - https://content.runescape.com/downloads/ubuntu/runescape.gpg.key | apt-key add -
mkdir -p /etc/apt/sources.list.d
echo "deb https://content.runescape.com/downloads/ubuntu trusty non-free" > /etc/apt/sources.list.d/runescape.list
apt-get update

wget http://ftp.us.debian.org/debian/pool/main/g/glew/libglew1.10_1.10.0-3_amd64.deb
dpkg -i libglew1.10_1.10.0-3_amd64.deb
wget -q -O /tmp/libpng12.deb http://mirrors.kernel.org/ubuntu/pool/main/libp/libpng/libpng12-0_1.2.54-1ubuntu1_amd64.deb \
  && dpkg -i /tmp/libpng12.deb \
  && rm /tmp/libpng12.deb

apt-get install -y libcurl3
apt-get install -y runescape-launcher
EOF

clear
echo "[*] Installation Complete! Launching RuneScape ..."
sleep 5s
runescape-launcher
rm install_runescape-nxt.py
rm libglew1.10_1.10.0-3_amd64.deb
clear
