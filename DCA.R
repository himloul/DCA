# Direct Clustering Algorithm

# examples
m = matrix(c(1,1,0,1,0,0,0,0,1,0,1,0,1,0,0,1,0,0,0,0,1,0,0,1,0,0,1,0,0,1),nrow = 6, ncol = 5)
m = matrix(c(1,1,0,1,0,0,0,0,1,0,1,0,1,0,0,1,1,0,0,0,1,0,0,1,0,0,1,0,0,1),nrow = 6, ncol = 5)
m = read.csv("C:/Users/Hamza/Documents/Facilities planning/part.machine.csv", sep = ";", header = FALSE)

m = data.frame(m)

#Step 1: Order the rows and columns.
m1 = data.frame(m)
m1 = m1[rev(order(rowSums(m1))), ] #rows in desc order, break ties by numerical descending order
m1 = m1[, rev(order(colSums(-m1)))] #cols in ascending order, break ties by numerical descending order

#Step 2: sort columns,
#shift column with 1 in the first row to the left
m2 = m1
for (i in c(1:ncol(m3),(ncol(m3)-1):1)) {
  m2 = m2[, order(-m2[i,])]
}

#Step 3:
m3 = m2
for (i in c(1:ncol(m3),(ncol(m3)-1):1)) {
  m3 = m3[order(-m3[,i]), ]
}

m3