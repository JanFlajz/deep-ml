import math
import numpy as np
def sigmoid(a):
	return round(1/(1+np.exp(-a)),4)
def mse(a,b):
	return ((a-b)**2).mean()

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
	features = np.array(features)
	labels = np.array(labels)
	weights = np.array(weights)
	res  =[]
	for f in features:
		res.append(sigmoid(np.dot(f, weights) + bias))
	er = mse(labels,np.array(res))


	return res, round(er,4)
