#!/usr/bin/env bash

# Deleting files
# Author: Emilio Figueras, 2020


echo "[+] Deleting log and output files"
echo "--> Deleting log output"
find /home/administrador/datos/freenet/logs -type f -delete
echo "--> Deleting spiders output"
find /home/administrador/datos/freenet/spiders/ongoing -type f -delete
find /home/administrador/datos/freenet/spiders/finished -type f -delete
echo "--> Deleting uuid.txt"
rm -f /home/administrador/RMAGAN/projects/I2P_Crawler/crawler/uuid.txt