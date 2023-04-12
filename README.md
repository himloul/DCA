# DCA  

*Direct Clustering Algorithm in R*  

**Direct clustering algorithm (DCA)** is a methodology for identification of cellular manufacturing structure within an existing manufacturing shop. The DCA was introduced in 1982 by H.M. Chan and D.A. Milner [1] The algorithm restructures the existing machine / component (product) matrix of a shop by switching the rows and columns in such a way that a resulting matrix shows component families (groups) with corresponding machine groups. See Group technology. The algorithm is executable in manual way but was already suitable for computer use of the time. [wikipedia](https://en.wikipedia.org/wiki/Direct_clustering_algorithm)  

### Algorithm
  
The DCA algorithm, also known as the "Direct Cluster Algorithm," is a method used in cellular manufacturing to create clusters of machines and parts that are optimally arranged to minimize material handling and increase productivity. Here is a rewritten version of the algorithm:

**Step 1: Order the rows and columns.**

Sum the number of 1s in each column and row of the machine-part matrix.  
Sort the rows in descending order of the number of 1s in each row.  
Sort the columns in ascending order of the number of 1s in each column.  
In case of a tie, break the tie in descending numerical sequence.

**Step 2: Sort the columns.**

Starting with the first row, shift to the left of the matrix all columns that have a 1 in that row.  
Continue this process row by row until no further opportunities exist for shifting columns.

**Step 3: Sort the rows.**

Starting with the leftmost column, shift rows upward when opportunities exist to form blocks of 1s.  
The column and row sortation can be facilitated using spreadsheets such as MS Excel.

**Step 4: Form cells.**

Look for opportunities to form cells such that all processing for each part occurs in a single cell.

## Usage

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