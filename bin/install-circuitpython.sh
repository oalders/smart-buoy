#!/bin/bash

set -x

#sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get install -y python3-pip
sudo pip3 install --upgrade setuptools
sudo pip3 install --upgrade adafruit-python-shell

# https://github.com/adafruit/Adafruit_CircuitPython_MPL3115A2
sudo pip3 install adafruit-circuitpython-mpl3115a2
