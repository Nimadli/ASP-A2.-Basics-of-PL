import numpy as np
import time

N, M, K = map(int, input("Enter matrix dimensions N, M, K: ").split())

np.random.seed(0)
A = np.random.rand(N, M)
B = np.random.rand(M, K)

start = time.perf_counter()

C = A @ B

end = time.perf_counter()

print(f"{end - start:.4f} seconds for {N}x{M} and {M}x{K} matrices")

# Unit test
A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[5, 6], [3, 4], [1, 2]])

start = time.perf_counter()

C = A @ B

end = time.perf_counter()

print(C)
print(f"{end - start:.4f} seconds for small matrices")