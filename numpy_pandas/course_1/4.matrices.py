import numpy as np

A = np.array([[1,2],[3,4]])

# A = A[:,0]

B = np.array([[1,2,3],[4,5,6]])

dot = A.dot(B)

# DETERMINANT AND INVERSE
det = np.linalg.det(A)
inv = np.linalg.inv(A)

# IDENTITY
id = np.linalg.inv(A).dot(A)

# TRACE
trc = np.trace(A)

# DIAGONAL
diag = np.diag(A)
# diag = np.diag([1,4])

# EIGENVALUE (eig1) AND EIGENVECTOR (eig2)
eig1 = np.linalg.eig(A)

Lam, V = np.linalg.eig(A)
# eig2 = V[:,0] * Lam[0] == A @ V[:,0] # [True, False]
# eig2 = V[:,0] * Lam[0], A @ V[:,0]

# allclose METHOD
# allc = np.allclose(V[:,0] * Lam[0], A @ V[:,0]) # True
allc = np.allclose(V @ np.diag(Lam), A @ V) # True

print(allc)