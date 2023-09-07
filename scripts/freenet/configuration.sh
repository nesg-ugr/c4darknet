#!/usr/bin/env bash

# Setting up crawling process config files
# Author: Emilio Figueras, 2020

# root path
root_path=~/RMAGAN/projects/I2P_Crawler

echo "[+] Setting up configuration files"
cp $root_path/scripts/config/settings.py $root_path/crawler/
cp $root_path/scripts/config/connection_settings.py $root_path/crawler/database/
cp $root_path/scripts/config/darknetsettings.py $root_path/crawler/darknet/
