import pandas as pd

df = pd.read_csv(r'D:\Downloads\de pe mac (coding projects)\myProjects\numpy_pandas\course_1\sbux.csv')

# head() shows 5 by default
df = df.head(10)

# tail() shows 5 by default
df = df.tail(10)

print(df)