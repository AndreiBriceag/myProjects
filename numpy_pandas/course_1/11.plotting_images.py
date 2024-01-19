import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

im = Image.open(r'D:\Downloads\de pe mac (coding projects)\myProjects\numpy_pandas\course_1\lena.png')
arr = np.array(im)

# BOTH OPTIONS WILL WORK
# plt.imshow(im)
# plt.imshow(arr)

gray = arr.mean(axis=2)
plt.imshow(gray, cmap='gray')


plt.show()

# print(arr)
# print(arr.shape)