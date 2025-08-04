#!/bin/bash

echo "Enter the file name : "
read filename
filename="${filename}.txt"

if [ -f "$filename" ]; then
	echo "File contents are : "
	cat "$filename"
else 
	echo "File doesn't exist"
fi


