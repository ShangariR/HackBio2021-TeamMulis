##Write a script that prints your name, your email, your slack username (with @) and your biostack, twitter_handle, hamming_distance in that order.##

install.packages("DescTools")
if (!require("remotes")) install.packages("remotes")
remotes::install_github("AndriSignorell/DescTools")
library(DescTools)

name <- "Sadaf Raza"
email <- "sadafraza48@gmail.com"
biostack <- "Genomics"
slack_username <- "@sadaf"
twitter_handle <- "@svdvf"

## Hamming distance
hamming_distance <- StrDist(slack_username, twitter_handle, method="hamming")


data <- data.frame(Information=c(name, email, slack_username, biostack, twitter_handle, hamming_distance))

rownames(data) <- c('NAME: ', 'E-MAIL: ', 'SLACK USERNAME: ', 'BIOSTACK: ', 'TWITTER HANDLE:','HAMMING DISTANCE:')

colnames(data) <- NULL
print(data)
