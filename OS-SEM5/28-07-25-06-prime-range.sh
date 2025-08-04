#!/bin/bash

echo "Enter an integer: "
read n
echo "Prime numbers up to $n are: "

for ((i=2; i<=n; i++)); do
  checkprime=1
  for ((j=2; j*j<=i; j++)); do
    if (( i % j == 0 )); then
      checkprime=0
      break
    fi
  done
  if (( checkprime == 1 )); then
    echo "$i"
  fi
done