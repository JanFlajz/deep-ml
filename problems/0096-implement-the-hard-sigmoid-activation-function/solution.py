def hard_sigmoid(x: float) -> float:
	"""
	Implements the Hard Sigmoid activation function.

	Args:
		x (float): Input value

	Returns:
		float: The Hard Sigmoid of the input
	"""
	if x < -3:
		return 0
	elif  x >=3:
		return 1
	return 0.2*x+0.5