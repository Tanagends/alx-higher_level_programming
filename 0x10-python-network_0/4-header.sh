#!/usr/bin/env bash
#Requests get to url and a header variable

if [ $# -lt 1 ]
then
  exit 1
else
  curl -sH "X-School-User-Id: 98" "$1"
fi
