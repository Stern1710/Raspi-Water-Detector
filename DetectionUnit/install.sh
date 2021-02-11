#!/bin/bash
if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

echo "--- If you get any disk space errors, run \"sudo raspi-config --expand-rootfs\" and then reboot"

echo "--- Updating and upgrading OS"
apt update
apt upgrade

echo "--- Installing SenseHat, MQTT and python packages"
apt install sense-hat python-gpiozero python-pip -y
pip install paho-mqtt

echo "--- Copy files to your wished directory now"
echo "--- IMPORTANT: Modify IP adress in getSensorData to correct MQTT server"
echo "--- IMPORTANT: Setup cronjob for correct path using this templace:"
echo "--- sudo crontab -e and go to the end of file"
echo "*/10 * * * * /usr/bin/python <full path to script>"