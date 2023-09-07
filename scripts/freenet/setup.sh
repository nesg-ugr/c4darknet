#!/usr/bin/env bash

# Deleting files
# Author: Emilio Figueras, 2020

root_path=~/RMAGAN/projects/I2P_Crawler

echo "[+] Creating folders..."
mkdir -p /home/administrador/datos/freenet/logs
mkdir -p /home/administrador/datos/freenet/spiders
mkdir -p /home/administrador/datos/freenet/spiders/ongoing
mkdir -p /home/administrador/datos/freenet/spiders/finished
echo " "

cd $root_path/crawler

echo "[+] Installing project dependencies ..."
source ~/anaconda3/etc/profile.d/conda.sh
conda activate py37
pip install -r requirements.txt
echo " "

echo "[+] Deleting log and output files"
echo "--> Deleting log output"
find /home/administrador/datos/freenet/logs -type f -delete
echo "--> Deleting spiders output"
find /home/administrador/datos/freenet/spiders/ongoing -type f -delete
find /home/administrador/datos/freenet/spiders/finished -type f -delete