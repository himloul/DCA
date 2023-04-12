'''Direct Clustering Algorithm using Python'''
import pandas as pd
import numpy as np

m = pd.read_csv("part.machine.csv", sep=";", header=None)

def dca(m):
    """
    Applies the Direct Clustering Algorithm (DCA) to a binary matrix `m` and returns the sorted binary matrix.

    Args:
        m (pandas.DataFrame): A binary matrix to be sorted by DCA. Rows represent items and columns represent features.
        
    Returns:
        pandas.DataFrame: The sorted binary matrix obtained by applying the DCA algorithm to `m`.
        
    The Direct Clustering Algorithm consists of the following steps:
    
    Step 1: Order the rows and columns.
    - Rows are ordered in descending order of their sum, breaking ties by numerical descending order.
    - Columns are ordered in ascending order of their sum, breaking ties by numerical descending order.
    
    Step 2: Sort columns.
    - Shift the column with 1 in the first row to the left.
    
    Step 3: Sort rows.
    - Sort the rows in descending order of the number of 1s they share with the first row.
    - Sort the columns as in Step 2, shifting the column with 1 in the first row to the left.
    """
    # Step 1: Order the rows and columns.
    m1 = m.copy()
    m1 = m1.iloc[np.argsort(-m1.sum(axis=1)), :]  # rows in desc order, break ties by numerical descending order
    m1 = m1.iloc[:, np.argsort(-m1.sum(axis=0))]  # cols in ascending order, break ties by numerical descending order

    # Step 2: sort columns,
    # shift column with 1 in the first row to the left
    m2 = m1.copy()
    for i in list(range(m2.shape[1])) + list(range(m2.shape[1] - 2, -1, -1)):
        m2.iloc[:, i] = m2.iloc[:, i].sort_values(ascending=False).reset_index(drop=True)

    # Step 3:
    m3 = m2.copy()
    for i in list(range(m3.shape[1])) + list(range(m3.shape[1] - 2, -1, -1)):
        m3.iloc[:, i] = m3.iloc[:, i].sort_values(ascending=False).reset_index(drop=True)

    return m3
