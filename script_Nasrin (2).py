name="Nasrin Parvin"
email="p.nasrin520@gmail.com"
slack_username="@Nasrin"
biostack="Genomics"
twitter_handle="@Nasrin123"


## calculating the hamming distance between stack_username and twitter handle##

string1 = slack_username
string2= twitter_handle
hamming_distance = 0

min_length = min(len(string1), len(string2))

for i in range(min_length):
     if string1[i] != string2[i]:
        hamming_distance += 1
      
    
print("Name:"+name,'Email:'+email,'Slack username:'+slack_username,'Biostack:'+biostack,'Twitter username :'+twitter_handle,hamming_distance,sep= "\n")