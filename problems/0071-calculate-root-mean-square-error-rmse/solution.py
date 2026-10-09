
import numpy as np

def rmse(y_true, y_pred):
	# Write your code here
	
	#a = np.subtract(y_pred, y_true)
	#b = np.power(a, 2)
	#c = np.mean(b)
	#print(np.sqrt(c))
	#print(a)
	#print(b)
	#print(np.mean([0.79056942, 0.70710678, 1.        ], axis=-1))

	y_pred = y_pred.flatten()
	y_true = y_true.flatten()
	rmse_res = np.sqrt(np.mean(np.power(np.subtract(y_pred, y_true), 2), axis=-1))
	#if rmse_res.shape:
	#	rmse_res = np.mean(rmse_res, axis=-1)
	

	return round(rmse_res,3)
