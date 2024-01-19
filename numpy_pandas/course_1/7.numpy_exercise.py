import numpy as np
from datetime import datetime

# ALSO WORKS WITH timeit

a = np.random.randn(100000)
b = np.random.randn(100000)
T = 100000

# def slow_dot_product(a, b):
#     result = np.matmul(a,b)
    
#     return result

t0 = datetime.now()
for t in range(T):
    np.matmul(a,b)
dt1 = datetime.now() - t0

t0 = datetime.now()
for t in range(T):
    a.dot(b)
dt2 = datetime.now() - t0

t0 = datetime.now()
for t in range(T):
    a @ b
dt3 = datetime.now() - t0

print("dt1: ", dt1.total_seconds())
print("dt2: ", dt2.total_seconds())
print("dt3: ", dt3.total_seconds())
print("dt1 / dt2: ", dt1.total_seconds() / dt2.total_seconds())