import numpy as np

def verifyMatrixMultiplication(A, B, C, t=10, atol=1e-10, rgen=None):
    rng = np.random.default_rng() if rgen is None else rgen
    n = A.shape[0]
    for _ in range(t):
        r = rng.integers(0, 2, size=(n, 1))   # r in {0,1}^n as column
        left  = A @ (B @ r)
        right = C @ r
        if not np.allclose(left, right, atol=atol, rtol=0.0):
            return False
    return True