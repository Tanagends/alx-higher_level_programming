#!/usr/bin/env bash
#Sends URL request and displays all the HTTP methods the server will accept

if [ $# -lt 1 ]
then
  exit 1
else
  curl -sI $1 | grep "Allow" | cut -d " " -f -2-
fi
