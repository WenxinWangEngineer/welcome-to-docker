import pandas as pd


# Read excel file from url or the same folder
# df = pd.read_excel('https://www.gairuo.com/file/data/dataset/team.xlsx')
df2 = pd.read_excel('team.xlsx')

# Print out read in data
# print(df)
print(df2)
# print(df2.head())         # == all rows
# print(df2.tail())         # == all rows
# print(df2.head(1))        # first 1 row
# print(df2.tail(2))        # last 2 rows
# print(df2.sample(4))      # random 5 rows


# print(df2.shape)          # check the row and column amounts
# print(df2.info())         # view index, dtype, and memory usage
# print(df2.describe())     # view the data type summary and statistics
# print(df2.dtypes)         # view dtypes of each data column
# print(df2.axes)           # view row and column axes
# print(df2.columns)        # view the column headers


# Build the index with name and take effect immediately
# print(df2.set_index('name', inplace=True))
# print(df2.index == 'Liver')
# print(df2)

# print(df2['Q1'])
# print(df2[['team', 'Q1']])    # view 2 columns: team and Q1
# print(df2.loc[:, ['team', 'Q1']])
# print(df2.name == 'Liver')    # return True for the name where is Liver

# print(df2[0:2])     # view first 2 rows
# print(df2[0:10:2])      # view every 2 rows in the first 10 rows
# print(df2.iloc[:10, :])     # view first 10 rows of data

# Only view Ben's 4 quarters
# print(df2.set_index('name', inplace=True))
# print(df2.loc['Ben', 'Q1':'Q4'])

# Order
# print(df2.sort_values(by='Q1'))     # default by ascending
# print(df2.sort_values(by='Q1', ascending=False))
# print(df2.sort_values(['team', 'Q1'], ascending=[True, False]))

# Conditions
# print(df2[df2.Q1 > 90])
# print(df2[df2.team == 'A'])
# print(df2.set_index('name', inplace=True))
# print(df2.index == 'Liver')
print(df2[(df2['team'] == 'C') & (df2['Q1'] > 90)])