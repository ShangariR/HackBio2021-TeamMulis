#!/usr/bin/env python3

Name = "R. Malavika"
Email = "malavikapunitha0211@gmail.com"
Slack_username = "@malavika"
Biostack = "Genomics, data science, software development, drug development, vaccine development"
Twitter_handle = "@malavikq"

## calculating the hamming distance between stack_username and twitter handle##

string1 = Slack_username
string2 = Twitter_handle
Hamming_distance = 0

min_length = min(len(string1), len(string2))

for i in range(min_length):
    if string1[i] != string2[i]:
        Hamming_distance += 1

print("{}, {}, {}, {}, {}, {}".format(Name, Email, Slack_username, Biostack, Twitter_handle, Hamming_distance))
