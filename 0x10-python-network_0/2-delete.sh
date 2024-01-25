#!/usr/bin/env bash
#Requests delete to url and displays response body

if [ $# -lt 1 ]
then
  exit 1
fi

curl -s $1
