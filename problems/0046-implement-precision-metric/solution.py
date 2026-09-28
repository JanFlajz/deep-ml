import numpy as np
def precision(y_true, y_pred):
	# Your code here
	assert  len(y_pred) == len(y_true)
	tp = fp = 0
	for i in range(len(y_pred)):
		if y_pred[i] == y_true[i] and y_pred[i]:
			tp += 1
		if y_pred[i] != y_true[i] and y_pred[i]:
			fp += 1
	if fp == 0 and tp == 0:
		return 0
	return tp/(tp + fp)


