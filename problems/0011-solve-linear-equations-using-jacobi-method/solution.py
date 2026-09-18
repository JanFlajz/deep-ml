import numpy as np
def count_sum(A,b,sol,i):
	_sum = 0
	for j in range(sol.shape[0]):
		if i != j:
			_sum += A[i][j] * sol[j]
	return _sum

def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
	sol = np.zeros(b.shape)
	for _ in range(n):
		tmp = np.zeros(b.shape)
		for i in range(sol.shape[0]):
			_sum = count_sum(A,b,sol,i)
			tmp[i] = (b[i] - _sum )/A[i][i]
		sol = tmp
				
		
	 
	return np.round(sol, 4).tolist()