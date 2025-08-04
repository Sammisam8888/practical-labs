#!/bin/bash

echo "Enter the file name : "
read filename
filename="${filename}.txt"

> "$filename"

echo "Hello guruji" >> "$filename"

echo "Contents successfully written to the file"
