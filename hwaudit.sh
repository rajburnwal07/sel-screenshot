#!/bin/bash
echo -e "\n *** Showing OS details *** \n"
cat /etc/os-release
echo -e "\n Kernel Version : $(uname -r)"
echo -e "\n CPU details "
cat /proc/cpuinfo
echo -e "\n *** RAM of machine *** \n"
#cat /proc/meminfo
free -h
echo -e "\n *** Network Configuration *** \n"
ifconfig -a
echo -e "\n *** showing open ports in firewall \n "
sudo firewall-cmd --list-all
echo -e "\n Showing mounted disks \n"
df -hT