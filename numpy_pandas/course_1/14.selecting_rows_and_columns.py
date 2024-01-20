import pandas as pd

df = pd.read_csv(r'D:\Downloads\de pe mac (coding projects)\myProjects\numpy_pandas\course_1\sbux.csv')

# To show all columns
# df = df.columns

# Rename columns
df.columns = (['date', 'open', 'high', 'low', 'close', 'volume', 'name'])
# print(df.head())


'''
Select specific columns
type(['open']) = <class 'pandas.core.series.Series'>
type([['open', 'close']]) = <class 'pandas.core.frame.DataFrame'>
'''
selected_columns = df[['open', 'close']] 
# print(selected_columns.head())
# print(type(selected_columns))


'''
Use df.iloc[0] when you want to access a row by its integer position.
Use df.loc['label'] when you want to access a row by its label (index).
'''
# df = df.iloc[0]
# df = df.loc[0]

# print(df)


# Loaded csv with specific index
# df2 = pd.read_csv(r'D:\Downloads\de pe mac (coding projects)\myProjects\numpy_pandas\course_1\sbux.csv', index_col='date')

# df2 = df2.loc['2013-02-08']

# print(df2)


# Filtering by ['open'] price > 64
df = df[df['open'] > 64]


# Filtering rows not named SBUX
df = df[df['name'] != 'SBUX']
# Result is empty because all rows are named SBUX
print(df)

# Save csv file without index column
smalldf = df[['open', 'close']]
smalldf.to_csv('output.csv', index=False)