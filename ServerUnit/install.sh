#!/bin/bash
if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

echo "--- If you get any disk space errors, run \"sudo raspi-config --expand-rootfs\" and then reboot"

echo "--- Updating and upgrading OS"
apt update
apt upgrade -y

echo "--- Installing MQTT-server and python packages"
apt install mosquitto python-gpiozero python-pip -y
pip install paho-mqtt mysql-connector-python

echo "--- Installing database starting secure installation"
apt install mariadb-server -y
mysql_secure_installation

echo "--- Setting up datebase: Enter the root password you just provided for the database"
mysql -u root -p < createDatabase.sql