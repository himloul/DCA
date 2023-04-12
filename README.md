# DCA  

*Direct Clustering Algorithm in R*  

**Direct clustering algorithm (DCA)** is a methodology for identification of cellular manufacturing structure within an existing manufacturing shop. The DCA was introduced in 1982 by H.M. Chan and D.A. Milner [1] The algorithm restructures the existing machine / component (product) matrix of a shop by switching the rows and columns in such a way that a resulting matrix shows component families (groups) with corresponding machine groups. See Group technology. The algorithm is executable in manual way but was already suitable for computer use of the time. [wikipedia](https://en.wikipedia.org/wiki/Direct_clustering_algorithm)  
  
This algorithm can be executed by the computer, using R


The Direct Clustering Algorithm is an implementation in R of a clustering algorithm that can be applied to binary data. This algorithm is based on three steps:

1. Order the rows and columns of the input matrix.
2. Sort the columns in a specific way.
3. Sort the rows in a specific way.

## **Usage**

To use the algorithm, you can start by defining a binary input matrix, **`m`**. There are different ways to create this matrix, for example, using the **`matrix()`** function or reading a CSV file using the **`read.csv()`** function.

```
m = read.csv("part.machine.csv", sep = ";", header = FALSE)

m = data.frame(m)
```

Once you have defined the input matrix, you can apply the Direct Clustering Algorithm.

## **Input**

The input matrix should be a binary matrix, where each row represents an observation and each column represents a feature. The values should be either 0 or 1.

## **Output**

The output of the algorithm is a binary matrix that has been reordered according to the Direct Clustering Algorithm. The rows and columns have been sorted in a specific way that aims to cluster together the observations that are most similar to each other.

## **Implementation**

The algorithm is implemented in R using built-in functions and loops. The steps of the algorithm are performed sequentially, and the output of each step is used as input for the next step.

The algorithm is designed to work with binary data, but it can be adapted to work with other types of data by changing the way the rows and columns are sorted.