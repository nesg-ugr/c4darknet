#!/usr/bin/env bash

# This scripts is in charge of starting the manager and saving the PID for afterward stopping it
# Author: Emilio Figueras, 2020

root_path=~/RMAGAN/projects/I2P_Crawler

cd $root_path/crawler

source ~/anaconda3/etc/profile.d/conda.sh
conda activate py37
python manager.py &>/dev/null &
pid=$!

echo "[+] Launching manager with PID=$pid"
echo $pid > pid.txt 