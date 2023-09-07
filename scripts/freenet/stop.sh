#!/usr/bin/env bash

# Stops the crawling process gracefully
# Author: Emilio Figueras, 2020

root_path=~/RMAGAN/projects/I2P_Crawler/crawler

echo "[+] Stopping crawling proces with UUID=`cat $root_path/uuid.txt`"
echo "--> Killing manager with PID=`cat $root_path/pid.txt`"
# stopping the manager (hard stop)
kill -9 `cat $root_path/pid.txt`
echo "--> Killing spiders ..."
# stopping spiders (hard stop)
kill -9 `pgrep scrapy`
