#!/usr/bin/env bash

# Dumping database
# Author: Emilio Figueras, 2020

data_path=/home/administrador/datos

echo "--> Dumping database"
mysqldump -u freenet -p1Uchn53d freenet_database > $data_path/i2p/freenet_database.sql






