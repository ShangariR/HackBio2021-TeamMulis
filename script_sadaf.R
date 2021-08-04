##Write a script that prints your name, your email, your slack username (with @) and your biostack in that order.##
name <- "Sadaf Raza"
email <- "sadafraza48@gmail.com"
Slack_username <- "@Sadaf"
biostack <- "Genomics"


data <- data.frame(Information=c(name, email, Slack_username, biostack))

rownames(data) <- c('NAME: ', 'E-MAIL: ', 'SLACK USERNAME: ', 'BIOSTACK: ')

colnames(data) <- NULL
print(data)
