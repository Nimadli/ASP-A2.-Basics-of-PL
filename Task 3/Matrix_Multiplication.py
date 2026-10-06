import numpy as np
import time

N = 1000

np.random.seed(0)
A = np.random.rand(N, N)
B = np.random.rand(N, N)

start = time.perf_counter()

C = A @ B

end = time.perf_counter()

print(f"{end - start:.4f} seconds for 1000x1000 matrices")

# Unit test
A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[5, 6], [3, 4], [1, 2]])

start = time.perf_counter()

C = A @ B

end = time.perf_counter()

print(C)
print(f"{end - start:.4f} seconds for small matrices")