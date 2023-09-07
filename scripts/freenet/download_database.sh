#!/usr/bin/env bash

# Restarting all the crawling processes on all the involved VMs.
# Author: Emilio Figueras, 2020

script_path=/home/administrador/RMAGAN/projects/I2P_Crawler/scripts/freenet
data_path=/home/administrador/datos

echo "[+] Dump database of freenetProjectBBDD"
ssh freenetProjectBBDD "cd $script_path; bash dump_database.sh"
echo " "

echo "[+] Download database freenet_database.sql"
scp freenetProjectBBDD:$data_path/i2p/freenet_database.sql freenet_database.sql
echo " "

echo "---- VM freenetProjectBBDD -----"
echo " "