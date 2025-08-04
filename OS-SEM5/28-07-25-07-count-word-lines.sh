#!/bin/bash

echo "Enter the file name: "
read file
file="${file}.txt"
if [ -f "$file" ]; then
  letter=$(wc -m < "$file")
  word=$(wc -w < "$file")
  line=$(wc -l < "$file")

  echo "File: $file"
  echo "Letters: $letter"
  echo "Words: $word"
  echo "Lines: $line"
else
  echo "File not found!"
fi
