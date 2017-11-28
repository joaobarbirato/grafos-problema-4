import numpy as np
import networkx as nx

A = np.loadtxt('./WG59/wg59_dist.txt')
G = nx.from_numpy_matrix(A)

