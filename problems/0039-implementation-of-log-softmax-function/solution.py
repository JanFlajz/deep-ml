import numpy as np

def log_softmax(scores: list) -> np.ndarray:
	# Your code here
	logs = np.array([np.exp(s - max(scores)) for s in scores])
	return np.log(logs/sum(logs))