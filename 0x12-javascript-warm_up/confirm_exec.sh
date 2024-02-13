#!/bin/bash

# This script confirms that the executable bit is set on a file.

for file in *;
do
	if [ -x "$file" ]
	then
		continue;
	else
		echo "$file is not executable";
		echo "Setting the executable bit on $file.....";
		chmod +x "$file";
	fi
done

# git add all files
echo "############################################
### ALL FILES HAVE BEEN MADE EXECUTABLE  ###
############################################"
read -p "Do you want to add all files to the repository? (y/n) " response
if [ "$response" = "y" ]
then
	git add .
	git commit -m "Add executable bit to all files"
	git push
fi

