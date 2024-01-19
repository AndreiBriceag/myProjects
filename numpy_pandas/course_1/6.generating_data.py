import numpy as np

zero = np.zeros((2,3))
one = np.ones((2,3))
ten = 10 * np.ones((2,3))

indentity = np.eye(3)

random = np.random.random()
random_matrix = np.random.random((2,3))
random_gaussian = np.random.randn(2,3)



R = np.random.randn(10000)

# mean of array R
R_mean = R.mean()
# R_mean = np.mean(R) # same as R above

# variant of array R
R_var = R.var()

#standard deviation (square root of the variant)
R_std = R.std()


R1 = np.random.randn(10000,3)
R1 = R1.mean(axis=0)
# R1 = R1.mean(axis=1).shape # the mean of 10000 rows and its shape


'''
When working with vectors, the analog of the variant is the covariant, cov()
'''
R2 = np.random.randn(10000,3)
# R2 = np.cov(R2).shape # (10000, 10000)
# R2 = np.cov(R2.T) # transpose (3, 3)
R2 = np.cov(R2, rowvar=False) # alternative

'''
Generate random integers in a specific range and size
'''
R3 = np.random.randint(0,10, size=(3, 3))
R4 = np.random.choice(10, size=(3, 3))

print(R4)