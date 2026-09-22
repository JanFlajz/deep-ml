import numpy as np
def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
	# Your code here

	X= data
	standrdized_data = (X - np.mean(X, axis=0)) / np.std(X, axis=0)
	


	normalized_data = (data - data.min(axis=0))/(data.max(axis=0) - data.min(axis=0))
	
	#print(standrdized_data)
	
	return standrdized_data,normalized_data