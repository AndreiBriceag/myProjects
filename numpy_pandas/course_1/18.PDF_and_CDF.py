import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Generate a range of x values from -6 to 6 with 1000 points
x = np.linspace(-6, 6, 1000)


'''
Calculate the PROBABILITY DENSITY FUNCTION (PDF) values for a normal distribution with mean (loc)=0 and standard deviation (scale)=1 at each x value
'''
fx = norm.pdf(x, loc=0, scale=1)

# Plot the normal distribution curve using x values and corresponding PDF values
plt.plot(x, fx)


'''
Calculate the CUMULATIVE DISTRIBUTION FUNCTION (CDF) values for a normal distribution with mean (loc)=0 and standard deviation (scale)=1 at each x value
'''
Fx = norm.cdf(x, loc=0, scale=1)

# Plot the cumulative distribution curve using x values and corresponding CDF values
plt.plot(x, Fx)


'''
Calculate the log PROBABILITY DENSITY FUNCTION (log PDF) values for a normal distribution with mean (loc)=0 and standard deviation (scale)=1 at each x value
'''
logfx = norm.logpdf(x, loc=0, scale=1)

# Plot the log probability density curve using x values and corresponding log PDF values
plt.plot(x, logfx)



# Display the plot
plt.show()