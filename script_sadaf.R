#!/usr/bin/env Rscript
name <- "Sadaf Raza"
email <- "sadafraza48@gmail.com"
biostack <- "Genomics"
slack_username <- "@sadaf"
twitter_handle <- "@svdvf"
#for hamming distance of slack_username between twitter_handle
#considering stringA for slack and stringB for twitter
stringA <- "@sadaf"
stringB <- "@svdvf"
count <- 0 # counter

# gets the number of characters in a string 
# Also gets if both are equal
# nchar counts the number of characters in a string.
min_length = min(nchar(stringA), nchar(stringB))

# converting strings to array of strings 
# using the strsplit function
stringA_split = strsplit(stringA, "")[[1]]
stringB_split = strsplit(stringB, "")[[1]]

for (i in 1:min_length){
  if (stringA_split[i] != stringB_split[i]){
    count = count + 1
  }
}

hamming_distance <- count


data <- data.frame(Information=c(name, email, slack_username, biostack, twitter_handle, hamming_distance))
rownames(data) <- c('NAME: ', 'E-MAIL: ', 'SLACK USERNAME: ', 'BIOSTACK: ', 'TWITTER HANDLE:','HAMMING DISTANCE:')

colnames(data) <- NULL
print(data)

