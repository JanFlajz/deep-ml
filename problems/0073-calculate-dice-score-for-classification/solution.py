
import numpy as np

def dice_score(y_true, y_pred):
	# Write your code here
	
	inter = 0
	for i in range(len(y_pred)):
		if y_pred[i] == y_true[i] and y_pred[i] and y_true[i]:
			inter += 1

	a = 0
	for i in range(len(y_pred)): 
		if y_pred[i]:
			a += 1
	b = 0
	for i in range(len(y_pred)): 
		if y_true[i]:
			b += 1

	#a = sum([i for i in range(len(y_pred)) if y_pred[i]])
	#b = sum([i for i in range(len(y_true)) if y_true[i]])



	if a ==0 and b == 0:
		return 0

	res = (2 * inter)/(a +b)
	
	return round(res, 3)
