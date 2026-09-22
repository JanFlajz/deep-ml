import numpy as np

def accuracy_score(y_true, y_pred):
	# Your code here
	acc = 0
	for i in range(len(y_true)):
		if y_pred[i] == y_true[i]:
			acc += 1

	return acc/len(y_true)