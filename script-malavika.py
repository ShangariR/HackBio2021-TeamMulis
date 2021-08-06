#!/usr/bin/env python3
name="R.Malavika"
email=" malavikapunitha0211@gmail.com"
slack_username="@malavika"
biostack="genomics,data science,software development,drug development,vaccines development"
twitter_Handle="@malavikq"

#calculating the hamming_distance between slack_username and twitter_handle

string1=slack_username
string2=twitter_handle

Hamming_distance = 0
min_length = min(len(string1), len(string2))

for i in range(min_length):
if string1[i] != string2[i]:
Hamming_distance += 1
print("{}, {}, {}, {}, {}, {}, {}".format(Name, Mail, Slack_Username, Biostack, Twitter_handle, hamming_distance))