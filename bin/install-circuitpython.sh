#!/bin/bash

set -x

#sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get install -y python3-pip
sudo pip3 install --upgrade setuptools
sudo pip3 install --upgrade adafruit-python-shell
sudo pip3 install adafruit-circuitpython-minimqtt
sudo pip3 install adafruit-io

# https://github.com/adafruit/Adafruit_CircuitPython_MPL3115A2
sudo pip3 install adafruit-circuitpython-mpl3115a2

git clone https://github.com/adafruit/Adafruit_IO_Python.git
cd Adafruit_IO_Python || exit
python3 setup.py install
