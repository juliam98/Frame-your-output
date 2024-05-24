#!/bin/bash

COL1='\033[44m' # blue
COL2='\033[42m' # green
NC='\033[0m' # No Color

width=$(tput cols)
height=$(($(tput lines) / 2 ))

print_w=$(echo "scale=0; $width/4" | bc)

for rows in $(seq 1 $height)
do
	
	for w in $(seq 1 $print_w)
	do
		echo -ne "$COL1  "
		echo -ne "$COL2  "
	done

	echo -ne "$NC"

	for w in $(seq 1 $print_w)
	do
		echo -ne "$COL2  "
		echo -ne "$COL1  "
	done

	echo -ne "$NC"
	echo -ne "\n"
	
done

