#!/usr/bin/env bash
#Requests post to url with variables

if [ $# -lt 1 ]
then
  exit 1
else
  curl -sX POST "$1" -d "name=test@gmail.com&subject=I will always be here for PLD"
fi
