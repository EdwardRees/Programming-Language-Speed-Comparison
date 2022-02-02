#!/bin/bash

if (($# != 1)); then
  echo "Usage: $0 <language>"
  exit 1
fi

if [ "$1" = "all" ]; then
  for i in {0..6}; do
    ./run.sh c $i
    ./run.sh c++ $i
    ./run.sh c# $i
    ./run.sh java $i
    ./run.sh python $i
    ./run.sh ruby $i
    ./run.sh javascript $i
    ./run.sh typescript $i
    ./run.sh lua $i
  done
else
  for i in {0..6}; do
    ./run.sh $1 $i
  done
fi
