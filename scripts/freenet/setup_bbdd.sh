#!/usr/bin/env bash

# Resetting database and schema
# Author: Emilio Figueras

root_path=~/RMAGAN/projects/I2P_Crawler/crawler
cd $root_path

echo "--> Deleting/creating database"
mysql -u freenet -p1Uchn53d -e "drop database freenet_database; create database freenet_database"

echo "--> Populate database"
source ~/anaconda3/etc/profile.d/conda.sh
conda activate py37
python populate.py
conda deactivate


