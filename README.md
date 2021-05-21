# Smart Buoy

<!-- vim-markdown-toc GFM -->

* [Logging in to the Pi](#logging-in-to-the-pi)
* [Installing inky phat libs](#installing-inky-phat-libs)
  * [Avoid the prompt](#avoid-the-prompt)
  * [Try examples](#try-examples)
* [Build Docker Image](#build-docker-image)
* [Test Script](#test-script)

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
