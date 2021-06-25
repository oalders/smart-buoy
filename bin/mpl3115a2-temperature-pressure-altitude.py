#!/usr/bin/python3

# SPDX-FileCopyrightText: 2019 Tony DiCola for Adafruit Industries
# SPDX-License-Identifier: MIT

# Simple demo of the MPL3115A2 sensor.
# Will read the pressure and temperature and print them out every second.
import time
import board
import adafruit_mpl3115a2

# Create sensor object, communicating over the board's default I2C bus
i2c = board.I2C()  # uses board.SCL and board.SDA

# Initialize the MPL3115A2.
sensor = adafruit_mpl3115a2.MPL3115A2(i2c)
# Alternatively you can specify a different I2C address for the device:
# sensor = adafruit_mpl3115a2.MPL3115A2(i2c, address=0x10)

# You can configure the pressure at sealevel to get better altitude estimates.
# This value has to be looked up from your local weather forecast or meteorological
# reports.  It will change day by day and even hour by hour with weather
# changes.  Remember altitude estimation from barometric pressure is not exact!
# Set this to a value in pascals:
sensor.sealevel_pressure = 102250

# Get MQTT details and more from a secrets.py file
try:
    from secrets import secrets
except ImportError:
    print("MQTT secrets are kept in secrets.py, please add them there!")
    raise

# Import library and create instance of REST client.
from Adafruit_IO import Client
aio = Client(secrets["aio_username"], secrets["aio_key"])

# Send the value 100 to a feed called 'Foo'.
aio.send('welcome-feed', 100)

# Main loop to read the sensor values and print them.
while True:
    pressure = sensor.pressure
    print("Pressure: {0:0.3f} pascals".format(pressure))
    print("Feed name: ", secrets["ambient_air_pressure_feed"])
    aio.send(secrets["ambient_air_pressure_feed"], pressure)
    altitude = sensor.altitude
    print("Altitude: {0:0.3f} meters".format(altitude))
    temperature = sensor.temperature
    print("Temperature: {0:0.3f} degrees Celsius".format(temperature))
    aio.send(secrets["ambient_temperature_feed"], temperature)
    time.sleep(180.0)
