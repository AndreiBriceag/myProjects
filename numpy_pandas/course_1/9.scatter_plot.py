import numpy as np
import matplotlib.pyplot as plt

x = np.random.randn(200, 2)
x[:50] += 3
y = np.zeros(200)
y[:50] = 1

plt.scatter(x[:,0], x[:,1], c=y)

plt.show()