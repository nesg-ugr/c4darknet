#!/usr/bin/env bash

# Pulling code remotely for all instances
# Author: Roberto Magan, 2019

if [ "$#" -lt 1 ]; then
  echo " "
  echo "Use: ./pull.sh <instances> <vm>"
  echo " "
  exit 1
fi

# list of all VM instances
vm_list=`cat $1`

# Remote scripts path
root_path=/home/administrador/RMAGAN/projects/I2P_Crawler

pull() {
  # $1 name of the remote VM
  vm=$1

  echo "[+] Pulling $vm from repository ..."
  # Checking out previous versions
  ssh $vm "cd $root_path; git checkout crawler/settings.py crawler/database/dbsettings.py crawler/database/entities.py; git pull;"
  echo " "

}

if [ "$#" -eq 2 ]; then
	vm=$2
	pull $vm
else

	# Deployment
	for vm in $vm_list;
	do
	  pull $vm
	done

fi
