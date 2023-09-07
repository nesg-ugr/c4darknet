#!/usr/bin/env bash

# Stopping all the related processes on all the involved VMs
# Author: Emilio Figueras, 2020

if [ "$#" -lt 1 ]; then
  echo " "
  echo "Use: ./stop_deployment.sh <instances> <vm>"
  echo " "
  exit 1
fi



# list of VM instances
vm_list=`cat $1`

# Remote scripts path
script_path=/home/administrador/RMAGAN/projects/I2P_Crawler/scripts/freenet

stop() {
  	# $1 name of the remote VM
  	vm=$1
  	echo "######### VM $vm ############"
	echo "[+] Stopping processes on $vm ..."
  	ssh $vm "cd $script_path; bash stop.sh"
  	echo " "
  	echo "---- VM $vm -----"
  	echo " "

}

if [ "$#" -eq 2 ]; then
	# Just only one VM
	vm=$2
	stop $vm
else

	# Deployment
	for vm in $vm_list;
	do
	  stop $vm
	done

fi

