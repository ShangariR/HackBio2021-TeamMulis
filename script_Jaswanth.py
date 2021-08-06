#!/usr/bin/env python3

name="JASWANTH D S"
email="jasdevshankar@gmail.com"
stack_username="@Jaswanth"
biostack="Genomics"
twitter_handle="@DsJaswan"


## calculating the hamming distance between stack_username and twitter handle##

#considering string1 for slack_usernmae and string2 for twitter_handle

string1 = stack_username
string2= twitter_handle
hamming_distance = 0

min_length = min(len(string1), len(string2))

for i in range(min_length):
     if string1[i] != string2[i]:
        hamming_distance += 1
      
    
print("Name:"+name,'Email:'+email,'Stack username:'+stack_username,'Biostack:'+biostack,'Twitter username :'+twitter_handle,sep= "\n")
print('Hamming Distance:',hamming_distance)





