import math
import numpy as np

A = np.array([[0, 1], [1, 1]], dtype=object)
for n in range(1, 10):
    An = np.linalg.matrix_power(A, n)
    print(f"n: {n}, A^n: {An.tolist()}")
    print(f"trace: {np.trace(An)}")
print("=" * 10)
print(
    f"limit of logN(p)/p: ",
    math.log(np.trace(np.linalg.matrix_power(A, 1 << 20))) / (1 << 20),
)
print(f"{math.log((1+math.sqrt(5))/2)=}")
