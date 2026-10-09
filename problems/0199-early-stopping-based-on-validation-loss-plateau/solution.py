def early_stopping(val_losses: list[float], patience: int = 5, min_delta: float = 0.0) -> list[bool]:
	"""
	Determine at each epoch whether training should stop based on validation loss.
	
	Args:
		val_losses: List of validation losses at each epoch
		patience: Number of epochs to wait for improvement before stopping
		min_delta: Minimum change in validation loss to qualify as improvement
	
	Returns:
		List of booleans indicating whether to stop at each epoch
	"""
	# Your code here
	idx = 0
	res = []
	
	for i,v in enumerate(val_losses):
		if i == 0:
			res.append(False)
			continue
		
		if (val_losses[i-1] -v) <= min_delta + 1e-9:
			idx += 1
		if idx < patience:
			res.append(False)
		elif idx >= patience:
			res.append(True)
			idx = 0
	return res
