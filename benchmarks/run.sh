#!/bin/bash

# get language, get function, pass into language runs
if (($# != 2)); then
  echo "Usage: $0 <language> <function>"
  exit 1
fi

if [ "$1" = "c" ]; then
  gcc -o main main.c
  echo ">> $2" >>results/c.txt
  for i in {0..9}; do
    ./main $2 >>results/c.txt
  done
elif [ "$1" = "cpp" ] || [ "$1" = "c++" ]; then
  g++ -o maincpp main.cpp
  echo ">> $2" >>results/c++.txt
  for i in {0..9}; do
    ./maincpp $2 >>results/c++.txt
  done
elif [ "$1" = "c#" ]; then
  csc main.cs
  echo ">> $2" >>results/c#.txt
  for i in {0..9}; do
    mono main.exe $2 >>results/c#.txt
  done
elif [ "$1" = "java" ]; then
  javac Main.java
  echo ">> $2" >>results/java.txt
  for i in {0..9}; do
    java Main $2 >>results/java.txt
  done
elif [ "$1" = "python" ]; then
  echo ">> $2" >>results/python.txt
  for i in {0..9}; do
    python3 main.py $2 >>results/python.txt
  done
elif [ "$1" = "ruby" ]; then
  echo ">> $2" >>results/ruby.txt
  for i in {0..9}; do
    ruby main.rb $2 >>results/ruby.txt
  done
elif [ "$1" = "javascript" ] || [ "$1" = "js" ]; then
  echo ">> $2" >>results/javascript.txt
  for i in {0..9}; do
    node main.js $2 >>results/javascript.txt
  done
elif [ "$1" = "typescript" ] || [ "$1" = "ts" ]; then
  echo ">> $2" >>results/typescript.txt
  for i in {0..9}; do
    ts-node main.ts $2 >>results/typescript.txt
  done
elif [ "$1" = "lua" ]; then
  echo ">> $2" >>results/lua.txt
  for i in {0..9}; do
    lua main.lua $2 >>results/lua.txt
  done
elif [ "$1" = "reset" ]; then
  if [ "$2" = "all" ]; then
    rm -f results/*.txt
    exit 0
  else
    rm -f results/$2.txt
    exit 0
  fi
elif [ "$1" = "clean" ]; then
  rm -f main maincpp main.exe Main.class
  exit 0
else
  echo "Invalid language"
  exit 1
fi
