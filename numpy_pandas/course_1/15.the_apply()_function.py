import pandas as pd

df = pd.read_csv(r'D:\Downloads\de pe mac (coding projects)\myProjects\numpy_pandas\course_1\sbux.csv')

def date_to_year(row):
    return int(row['date'].split('-')[0])

# Axis=1 for rows, Axis=0 for columns
# df = df.apply(date_to_year, axis=1)
df['year'] = df.apply(date_to_year, axis=1)

print(df.head())