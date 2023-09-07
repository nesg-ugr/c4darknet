#!/usr/bin/env bash

# Setup, configure and run all the crawling processes on all the involved VMs
# Author: Emilio Figueras, 2020

if [ "$#" -lt 1 ]; then
  echo " "
  echo "Use: ./start_deployment.sh <instances> <vm>"
  echo " "
  exit 1
fi


# list of VM instances
vm_list=`cat $1`

# Remote scripts path
script_path=/home/administrador/RMAGAN/projects/I2P_Crawler/scripts/freenet

deploy() {
  # $1 name of the remote VM
  vm=$1
  echo "######### VM $vm ############"

  bash pull.sh fake.txt $vm
  echo " "

  echo "[+] Configuring crawling process on $vm ..."
  ssh $vm "cd $script_path; bash configuration.sh"
  echo " "

  # Reseting BBDD and schema
  if [ $vm == 'freenetProjectBBDD' ]
  then
  	echo "[+] Setting up the file environment $vm ..."
  	ssh $vm "cd $script_path; bash setup_bbdd.sh"
  	echo " "
  else
    echo "[+] Setting up the file environment $vm ..."
  	ssh $vm "cd $script_path; bash setup.sh"
  	echo " "

    # Starting crawling process for VMs different from the VMs
    echo "[+] Starting the crawling process on $vm ..."
  	ssh $vm "cd $script_path; bash start.sh $vm"
  	echo " "
  fi
 
  echo "---- VM $vm -----"
  echo " "

}

if [ "$#" -eq 2 ]; then
	vm=$2
	deploy $vm
else

	# Deployment
	for vm in $vm_list;
	do
	  deploy $vm
	  echo "[+] Waiting 1 mins ..."
	  sleep 1m
	done

fi

