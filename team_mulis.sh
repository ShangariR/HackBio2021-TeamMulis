#!/usr/bin/env bash
#command to clone the team mulis repo
git clone https://github.com/pragnapcu/HackBio2021-TeamMulis.git

# changing directory into the repo

cd ./HackBio2021-TeamMulis

#adding right to execute the script in the repo
chmod +x script*

#for loop below for executing all the scripts in this repo and producing output as csv file

for i in $(ls script*)
do
	        ./$i | awk -F ',' '{OFS="\t";print $1, $2, $3, $4, $5, $6}' >> Team_Mulis.csv
	done
