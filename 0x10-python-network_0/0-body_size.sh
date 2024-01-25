#!/usr/bin/env bash
#Sends a request to an URL and displays the size of the response

if [ $# -lt 1 ]
then
  exit 1
else
  curl -s $1 | wc -c
fi
