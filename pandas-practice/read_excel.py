import pandas as pd


# Read excel file from url or the same folder
# df = pd.read_excel('https://www.gairuo.com/file/data/dataset/team.xlsx')
df2 = pd.read_excel('team.xlsx')

# Print out read in data
# print(df)
# print(df2)
# print(df2.head())  # == all rows
# print(df2.tail())  # == all rows
# print(df2.head(1))  # first 1 row
# print(df2.tail(2))  # last 2 rows
print(df2.sample(4))  # random 5 rows


# print(df2.shape)  # check the row and column amounts
# print(df2.info())
