#! /usr/bin/bash
clear
sleep 1
apt update & upgrade

read -p "enter "

echo "WELCOME TO PAGE "

echo " "
echo "OPTIONS are "
echo "1 for call"


read -p "enter the options " opt
sleep 1

if [[ $opt -eq 1 ]];then
  echo " 1 all ok "
  echo " 2 suman  "
  echo " 3 khlish "
  echo " 4 yugal "
  read -p "enter the name to call " num
  if [[ $num -eq 1 ]];then
     termux-telephony-call 7000020324
  elif [[ $num -eq 2 ]];then
     termux-telephony-call 7748820049
  elif [[ $num -eq 3 ]];then
     termux-telephony-call 8770764657
  elif [[ $num -eq 4 ]];then
     termux-telephony-call 7999794187
  else
    echo "enter valid name"
  fi
else
  echo "enter valid number"
fi
