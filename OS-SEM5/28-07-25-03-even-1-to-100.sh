#!/bin/bash

echo "Even numbers from 1 to 100 is : "

for ((i=1;i<=100;i++))
do
	if ((i%2==0)); then
		echo "$i"
	fi
done
