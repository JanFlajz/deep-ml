import numpy as np
def disorder(apples: list) -> float:
	"""
	Compute the disorder in a basket of apples.
	"""
	# Your code here
	unique, counts = np.unique(apples, return_counts=True)
	probs = dict(zip(unique, counts))
	for p in probs:
		probs[p] /= len(apples) 
	entropy = 0
	for p in probs:
		entropy -= probs[p] * np.log(probs[p])
	#print(entropy)
	return entropy
	#return unique,counts