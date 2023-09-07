#!/usr/bin/env bash

# Run all cleaning processes on all the involved VMs
# Author: Emilio Figueras, 2020

if [ "$#" -lt 1 ]; then
  echo " "
  echo "Use: ./clean_deployment.sh <instances> <vm>"
  echo " "
  exit 1
fi


# list of VM instances
vm_list=`cat $1`

# Remote scripts path
script_path=/home/administrador/RMAGAN/projects/I2P_Crawler/scripts/freenet

cleaning() {
  # $1 name of the remote VM
  	vm=$1
  	echo "######### VM $vm ############"


	# Starting crawling process for VMs different from the VMs
	echo "[+] Starting the cleaning process on $vm ..."
	ssh $vm "cd $script_path; bash clean.sh $vm"
	echo " "

 
  	echo "---- VM $vm -----"
  	echo " "

}

if [ "$#" -eq 2 ]; then
	vm=$2
	cleaning $vm
else

	# Cleaning
	for vm in $vm_list;
	do
	  cleaning $vm
	done

fi

