#!/usr/bin/env bash
#Requests get to url and displays body if Status code is 200

if [ $# -lt 1 ]
then
  exit 1
fi

response=$(curl -s -w "%{http_code}" "$1")
if [ "$response" -eq "200" ]
then
  curl -s $1
fi
