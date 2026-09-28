import numpy as np

def make_diagonal(x):
	# Your code here
	z = np.zeros((x.shape[0], x.shape[0]))
	for i in range(len(x)):
		z[i][i] = x[i]
	return z