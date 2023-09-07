#!/usr/bin/env bash

# Check the status of servers and crawling processes on the involved VMs
# Author: Emilio Figueras, 2020

if [ "$#" -lt 1 ]; then
  echo " "
  echo "Use: ./status.sh <instances> <vm>"
  echo " "
  exit 1
fi

# list of all VM instances
vm_list=`cat $1`

get_status() {
  # $1 name of the remote VM
  vm=$1

  echo "[+] Crawling process status on $vm ..."
  ssh $vm "ps -ef | grep 'python.*m[a]nager'"
  echo " "

  echo "[+] Number of spiders in ongoing status on $vm ..."
  ssh $vm "ps -ef | egrep 'scrapy.*c[r]awl' | wc -l"
  echo " "

  echo "[+] Number of spiders in defunct status on $vm ..."
  ssh $vm "ps axo pid,stat,args | grep scrapy | awk '\$2 ~ /^Z/ { print \$1 }' | wc -l"
  echo " "

  echo "[+] HD status on $vm ..."
  ssh $vm "df -kh | grep -e \"sd\""
  echo " "
  
  echo "[+] MEM status on $vm ..."
  ssh $vm "free -h"
  echo " "

  echo "---- VM $vm -----"
  echo " "
  echo " "

}

if [ "$#" -eq 2 ]; then
	vm=$2
	get_status $vm
else

	# Deployment
	for vm in $vm_list;
	do
	  get_status $vm
	done

fi







