#!/usr/bin/env python3

def hammingDist(str1, str2):
	i = 0
	count = 0
	while(i < len(str1)):
		if(str1[i] != str2[i]):
			count += 1
		i += 1
	return count
str1 = "Preeti"
str2 = "pretty"

Name=("Preeti")
Email=("contactpreetiat3@gmail.com")
Slack_username=("@Preeti")
Biostack=("Genomics and Transciptomics")
Twitter_handle=("@pretty")
Hamming_distance=(hammingDist)

print("{}, {}, {}, {}, {}, {}".format(Name, Email, Slack_username, Biostack, Twitter_handle, Hamming_distance))
