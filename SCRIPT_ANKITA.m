#! usr/bin/env octave

name = "Ankita Banubakode";
email = "banubakodeankita@gmail.com"; 
slack_username = "@Anku";
biostack = "Genomics" ;
twitter_username = "@Anku" ; 

min_length = min(length(slack_username), length(twitter_username));
hamming_distance = 0

for i=1:min_length;
if (slack_username(i) != twitter_username);
   hamming_distance = hamming_distance + 1;
  endif
endfor

printf("%s, %s, %s, %s, %s, %i", name, email, slack_username, 
biostack, twitter_username, hamming_distance)
 





