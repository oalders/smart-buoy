# Smart Buoy

<!-- vim-markdown-toc GFM -->

  * [Logging in to the Pi](#logging-in-to-the-pi)
  * [Installing inky phat libs](#installing-inky-phat-libs)
    * [Avoid the prompt](#avoid-the-prompt)
    * [Try examples](#try-examples)
  * [Build Docker Image](#build-docker-image)
  * [Test Script](#test-script)
* [Install CircuitPython](#install-circuitpython)
* [Enable I2C](#enable-i2c)
* [Attach mpl3115a2 Sensor](#attach-mpl3115a2-sensor)

<!-- vim-markdown-toc -->

## Logging in to the Pi

```sh
ssh pi@raspberrypi.local
```


## Installing inky phat libs

```sh
curl https://get.pimoroni.com/inky | bash
```

### Avoid the prompt

```sh
curl https://get.pimoroni.com/inky | bash -s -- -y
```

### Try examples

```sh
cd /home/pi/Pimoroni/inky/examples
```

## Build Docker Image

```sh
docker build . -t smartbuoy
```

## Test Script

```sh
docker run -it --volume $PWD:/home/smartbuoy smartbuoy:latest /bin/bash -c "cd /home/smartbuoy && /bin/bash"
docker run -it --volume $PWD:/home/smartbuoy smartbuoy:latest /bin/bash -c "cd /home/smartbuoy && python3 inky.py"
```
# Install CircuitPython

```
scp bin/install-circuitpython.sh pi:~/
scp bin/blinka-test.py pi:~/
ssh pi
bash install-circuitpython.sh
```

# Enable I2C

`sudo raspi-config` on the command line, then use the arrow keys to select 'Interfacing Options' and 'I2C' to tell the RasPi to enable the I2C interface. Then select 'Finish' and reboot

# Attach mpl3115a2 Sensor

https://learn.adafruit.com/using-mpl3115a2-with-circuitpython/circuitpython
