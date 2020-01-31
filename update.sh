#!/bin/sh

## This is Linux OS Update Script ##


## Getting System Information
sudo hostname >> host
echo Starting installing OS updates for hostname $host
sudo hostname
sudo date
sudo uname -a
sudo cat /etc/redhat-release

## Installing Red Hat Linux OS Updates



sudo yum -y update

echo Updates Finished.
## Getting Updated System Information

sudo date
sudo uname -a
sudo cat /etc/redhat-release

## Restarting System After OS Updates

echo Restarting the server

#echo "Restart server now (yes or n)?"
#read ln
#if [ $ln == "yes" ]
#then
       sudo shutdown -r +1
#fi


## Command to execute this script in Linux ##
###     ./linuxOSupdate.sh 2>&1 | tee -a linuxupdate.txt
