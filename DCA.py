'''Direct Clustering Algorithm using Python'''
import pandas as pd
import numpy as np
import argparse
from main import dca_algorithm, dca

m = pd.read_csv("part.machine.csv", sep=";", header=None)

dca_algorithm(m)

result_matrix = dca(m)

print(result_matrix)

