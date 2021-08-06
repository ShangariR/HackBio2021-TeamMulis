#!/usr/bin/env python3

Name = ("Preeti")
Email = ("contactpreetiat3@gmail.com")
Slack_username = ("@Preeti")
Biostack = ("Genomics and Transcriptomics")
Twitter_handle = ("@pretty")
Hamming_distance = ("hamming_distance")

## calculating the hamming distance between stack_username and twitter handle##

# considering string1 for slack_usernmae and string2 for twitter_handle

string1 = Slack_username
string2 = Twitter_handle
hamming_distance = 0

min_length = min(len(string1), len(string2))

for i in range(min_length):
    if string1[i] != string2[i]:
        hamming_distance += 1

print("{}, {}, {}, {}, {}, {}".format(Name, Email, Slack_username, Biostack, Twitter_handle, hamming_distance))
