import numpy as np

def batch_iterator(X, y=None, batch_size=64):
	array = []
	for i in range(0, len(X), batch_size):
		res = None
		if y is not None:
			res = [X[i:i + batch_size],y[i:i + batch_size]]
		else:
			res = [X[i:i + batch_size]]

		#res.append(y[i:i + batch_size])
		array.append(res)
	return array
		
	
