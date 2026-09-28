import numpy as np
def softsign(x: float) -> float:
	"""
	Implements the Softsign activation function.

	Args:
		x (float): Input value

	Returns:
		float: The Softsign of the input
	"""
	# Your code here
	result = x/(np.abs(x) + 1)
	return round(result, 4)