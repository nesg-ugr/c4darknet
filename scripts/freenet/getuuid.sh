#!/usr/bin/env bash

# Stopping all the related processes on all the involved VMs
# Author: Emilio Figueras, 2020

if [ "$#" -lt 1 ]; then
  echo " "
  echo "Use: ./getuuid.sh <instances> <vm>"
  echo " "
  exit 1
fi



# list of VM instances
vm_list=`cat $1`

# Remote scripts path
root_path=/home/administrador/RMAGAN/projects/I2P_Crawler/crawler

stop() {
  # $1 name of the remote VM
  vm=$1

  if [ $vm != 'freenetProjectBBDD' ]
  then
  	
  	uuid=`ssh $vm "cd $root_path; cat uuid.txt"`
	echo "'$uuid':'$vm'"
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
