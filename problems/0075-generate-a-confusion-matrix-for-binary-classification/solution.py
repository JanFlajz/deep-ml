
from collections import Counter

def confusion_matrix(data):
	# Implement the function here
	true_pos = false_pos = false_neg = true_neg = 0
	for tup in data:
		if tup[0]:
			if tup[1]:
				true_pos += 1
			else:
				false_neg += 1
		else:
			if tup[1]:
				false_pos += 1
			else:
				true_neg += 1
			 

	return [[true_pos,false_neg],[false_pos,true_neg]]
	
