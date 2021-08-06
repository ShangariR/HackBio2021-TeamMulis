#!/usr/bin/env bash

output="$1"

git clone https://github.com/pragnapcu/HackBio2021-TeamMulis
cd HackBio2021-TeamMulis

(
g++ script_Shangari.cpp -o script_Shangari && ./script_Shangari
perl script_Vishnupriya.pl
python3 script_Preeti.py
) > ../"$output"

