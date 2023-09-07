#!/usr/bin/env bash

# Restarting all the crawling processes on all the involved VMs.
# Author: Emilio Figueras, 2020

if [ "$#" -lt 1 ]; then
  echo " "
  echo "Use: ./restart_deployment.sh <instances> <vm>"
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

  # Starting crawling process for VMs different from the VMs
  echo "[+] Re-starting the crawling process on $vm ..."
  ssh $vm "cd $script_path; bash start.sh $vm"
  echo " "
 
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
	  #echo "[+] Waiting 1 mins ..."
	  #sleep 1m
	done

fi

