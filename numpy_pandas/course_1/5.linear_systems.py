import numpy as np

'''
The admission fee at a festival is $1.50 for children and $4.00 for adults.
On a certain day, 2200 people enter the fair, and $5500 is collected.
How many children and how many adults entered?

Ans: 1500 children and 700 adults
'''

A = np.array([[1,1],[1.5,4]])
B = np.array([2200, 5050])

sol = np.linalg.solve(A,B)

print(sol)