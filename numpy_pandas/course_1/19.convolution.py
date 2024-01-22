import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from PIL import Image
from scipy.signal import convolve2d

# Open the Lena image
im = Image.open(r'D:\Downloads\de pe mac (coding projects)\myProjects\numpy_pandas\course_1\lena.png')

# Convert the image to grayscale by taking the mean along the third axis
gray = np.mean(im, axis=2)

# Generate a 1D array of values from -6 to 6 with 50 points
x = np.linspace(-6, 6, 50)

# Create a 1D Gaussian distribution using scipy's norm.pdf function
fx = norm.pdf(x, loc=0, scale=1)

# Create a 2D filter by taking the outer product of the 1D Gaussian distribution
filt = np.outer(fx, fx)

# Uncomment the line below to visualize the 2D filter
# plt.imshow(filt, cmap='gray')

# Use scipy's convolve2d function to convolve the grayscale image with the 2D filter
out = convolve2d(gray, filt)

# Plot the original grayscale image and the filtered output side by side
plt.subplot(1, 2, 1)
plt.imshow(gray, cmap='gray')
plt.title('Original Grayscale Image')

plt.subplot(1, 2, 2)
plt.imshow(out, cmap='gray')
plt.title('Filtered Image')

# Display the plot
plt.show()

'''This code loads an image, converts it to grayscale, creates a 2D Gaussian filter, convolves the filter with the grayscale image, and then displays the original grayscale image and the filtered output side by side. The commented line (plt.imshow(filt, cmap='gray')) can be uncommented to visualize the 2D filter if needed.'''
