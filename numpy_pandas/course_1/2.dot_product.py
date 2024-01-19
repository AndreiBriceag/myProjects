import numpy as np

a = np.array([1,2])
b = np.array([3,4])

dot = 0

# THE BELOW EXERCISES ARE SIMILAR EXAMPLES

# for e, f in zip(a, b):
#     dot += e * f

# for i in range(len(a)):
#     dot += a[i] * b[i]

# dot = np.sum(a * b)
# dot = (a * b).sum()

# THIS IS THE ACTUAL WAY OF DOING IT (3 OPTIONS)

# dot = a @ b
# dot = a.dot(b)
# dot = np.dot(a, b)

# LINEAL ALGORITHM 

# amag = np.sqrt((a * a).sum())
# norma = np.linalg.norm(a)

cosangle = a.dot(b) / (np.linalg.norm(a) * np.linalg.norm(b))
angle = np.arccos(cosangle)

# print(dot)
# print(amag)
# print(norma)
# print(cosangle)
print(angle)
