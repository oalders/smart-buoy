#!/bin/bash

pip3 install virtualenv
virtualenv my_phat_env
cd my_phat_env || exit 1
source bin/activate
cd -
./my_phat_env/bin/pip3 install -r requirements.txt
