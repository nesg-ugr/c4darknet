#!/usr/bin/env bash

# Stopping all the related processes on all the involved VMs
# Author: Emilio Figueras, 2020

if [ "$#" -lt 1 ]; then
  echo " "
  echo "Use: ./status.sh <instances> <vm>"
  echo " "
  exit 1
fi



# list of VM instances
vm_list=`cat $1`

# Remote scripts path
script_path=/home/administrador/RMAGAN/projects/c4darknet/scripts/c4darknet/

stop() {
  	# $1 name of the remote VM
  	vm=$1
  	
  	# Nothing to check for the vm hosting the BBDD
  	if [ $vm != 'c4darknet10' ]
  	then
  	
  		echo "######### VM $vm ############"
		echo "[+] Crawling status on $vm ..."
  		ssh $vm "cd $script_path; tail -n 500 ~/datos/c4darknet/logs/darknetcrawler.log | grep ONGOING | tail -n 1"
  		echo " "
  		echo "---- VM $vm -----"
  		echo " "
  	fi

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

