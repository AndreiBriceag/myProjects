import numpy as np
import matplotlib.pyplot as plt

'''
Optional random seed for initializing the random number generator with a fixed value.
This is particularly useful when you want to share your code with others or when you need to ensure that the randomness does not affect the results during development or testing.
By setting the seed, you can make sure that the random numbers generated in different runs of the code remain the same, providing consistency in your experiments or simulations.
'''
# np.random.seed(42)

# Function to generate XOR dataset
def generate_xor_dataset(size):
    X = np.random.rand(size, 2) * 2 - 1  # Random points in the range [-1, 1]
    y = np.logical_xor(X[:, 0] > 0, X[:, 1] > 0).astype(int)  # XOR labels
    
    return X, y

# Generate XOR dataset with 2000 points
data_size = 2000
X_xor, y_xor = generate_xor_dataset(data_size)

# Plot the XOR dataset
plt.scatter(X_xor[y_xor == 0][:, 0], X_xor[y_xor == 0][:, 1], c='purple', label='Absolute')
plt.scatter(X_xor[y_xor == 1][:, 0], X_xor[y_xor == 1][:, 1], c='orange', label='Mixed')
plt.title('XOR Dataset')
plt.xlabel('Axis X')
plt.ylabel('Axis Y')
plt.xlim(-1, 1)  # Set x-axis range
plt.ylim(-1, 1)  # Set y-axis range
plt.legend()
plt.show()
