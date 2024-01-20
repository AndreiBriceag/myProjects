import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix


df = pd.read_csv(r'D:\Downloads\de pe mac (coding projects)\myProjects\numpy_pandas\course_1\sbux.csv')

# Create a histogram of the 'open' column
# df['open'].hist()

# Create a line graph of the 'open' column
# df['open'].plot()

# Create a boxplot of the 'open', 'high', 'low', 'close' columns
# df[['open', 'high', 'low', 'close']].plot.box()

'''
Create a scatter matrix
alpha=0.2 maxes dots have transparency
figsize=(6, 6) makes the plot bigger
'''
scatter_matrix(df[['open', 'high', 'low', 'close']], alpha=0.2, figsize=(6, 6))

plt.show()