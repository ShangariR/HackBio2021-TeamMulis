#include <stdio.h>
#include <string.h>

int main(void)
{
    char name[30] = "Chigozie Nkwocha";
    char email[80] = "bueze25@gmail.com";
    char slack_username[80] = "GozieNkwocha";
    char biostack[100] = "Transcriptomics";
    char twitter[15] = "Gozi251";
    
	int min_length;
    int hamming_distance = 0;
    int twitter_len = strlen(twitter);
    int slackusername_len = strlen(slack_username);

    if (twitter_len < slackusername_len){
        min_length = twitter_len;
    }
    else if (slackusername_len < twitter_len){
        min_length = slackusername_len;
    }
    else{
        min_length = slackusername_len;
    }
	
	for(int i=0; i<min_length; i++){
        if (twitter[i] != slack_username[i]){
            hamming_distance += 1;
        }
    }
    printf("%s \n", name);
    printf("%s \n", email);
    printf("@%s \n", slack_username);
    printf("%s \n", biostack);
    printf("@%s\n", twitter);
    printf("%i\n", hamming_distance);
    return 0;
}

