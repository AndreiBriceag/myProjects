import numpy as np

L = [1,2,3]

A = np.array([1,2,3])

# THIS IS THE ACTUAL WAY OF DOING ITCAN APPEND NEW ITEMS TO A LIST, BUT NOT TO AN ARRAY
# L.append(4)
# L = L + [5]

# ADDS +4 TO EACH ELEMENT OF ARRAY A (BROADCAST)
# A = A + np.array([4])

# ADDS 2 ARRAYS TO, TE EACH ELEMENT (BROADCAST)
# A = A + np.array([4,5,6])

# ERROR! CANNOT ADD VECTORS OF DIFFERENT SIZES
# A = A + np.array([4,5])

# CAN MULTIPLY A VECTOR; A = [2 4 6]
# A = A * 2

# CAN MULTIPLY A LIST; L = [1, 2, 3, 1, 2, 3]
# L = L * 2
# L = L + L

# ADD 5 TO EACH ELEMENT IN LIST WITH FOR LOOP
# L2 = []
# for e in L:
#     L2.append(e + 5)

# ADD 5 TO EACH ELEMENT IN LIST WITH LIST COMPREHENTION
# L2 = [e + 5 for e in L]

# SQUARE OF LIST L2
# L2 = []
# for e in L:
#     L2.append(e**2)

# SQUARE OF ARRAY A
# A = A**2

# SQUARE ROOT OF ARRAY A
# A = np.sqrt(A)

# LOGARITHM (log) OF ARRAT A
# A = np.log(A)

# EXPONENTIAL OF ARRAY A
# A = np.exp(A)

# HYPERBOLIC TENSION OF ARRAY A
A = np.tanh(A)


print(A)
# print(L)
# print(L2)