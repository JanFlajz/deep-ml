
from collections import Counter

def confusion_matrix(data):
	# Implement the function here
	true_pos = sum(x and y for x,y in data)
	false_pos = sum(not x and y for x,y in data)
	false_neg = sum(x and not y for x,y in data)
	true_neg = sum(not x and not y for x,y in data)

			 

	return [[true_pos,false_neg],[false_pos,true_neg]]
	
