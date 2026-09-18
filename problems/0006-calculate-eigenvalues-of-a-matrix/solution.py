import numpy as np
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	eigenvalues,eigenvectors = np.linalg.eigvals(np.array(matrix))
	return list((eigenvalues,eigenvectors))