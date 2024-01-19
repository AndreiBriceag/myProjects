import numpy as np
import matplotlib.pyplot as plt

# x = np.random.randn(10000)
# plt.hist(x, bins=100) # bins= number of bars in the histogram

x = np.random.random(10000)
plt.hist(x, bins=100)

plt.show()