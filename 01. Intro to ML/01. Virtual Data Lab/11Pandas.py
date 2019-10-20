# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# %% create a dataframe

columns = ['name', 'age', 'gender', 'job']
user1 = pd.DataFrame([['alice', 19, "F", "student"],
['john', 26, "M", "student"]],
columns=columns)

user2 = pd.DataFrame([['eric', 22, "M", "student"],
['paul', 58, "F", "manager"]],
columns=columns)

user3 = pd.DataFrame(dict(name=['peter', 'julie'],
age=[33, 44], gender=['M', 'F'],
job=['engineer', 'scientist']))
print(user3)

# %% concatenate dataframe
user1.append(user2)
users = pd.concat([user1, user2, user3])
print(users)

# %% join dataframe 

user4 = pd.DataFrame(dict(name=['alice', 'john', 'eric', 'julie'],
height=[165, 180, 175, 171]))
print(user4)

# join
merge_inter = pd.merge(users, user4, on="name")
print(merge_inter)

#outer join
users = pd.merge(users, user4, on="name", how='outer')
print(users)

# %% pivot a dataframe into key, variable, value structur
staked = pd.melt(users, id_vars="name", var_name="variable", value_name="value")
print(staked)

# %% pivot a dataframe from melted one
back_df =staked.pivot(index='name', columns='variable', values='value')
print(back_df)

# %% analyse dataframe content
users # print the first 30 and last 30 rows
type(users) # DataFrame
users.head() # print the first 5 rows
users.tail() # print the last 5 rows
users.index # "the index" (aka "the labels")
users.columns # column names (which is "an index")
users.dtypes # data types of each column
users.shape # number of rows and columns
users.values # underlying numpy array
users.info() # concise summary (includes memory usage as of pandas 0.15.0)

# %% select columns

#single column selection
users['gender'] # select one column
type(users['gender']) # Series
users.gender # select one column using the DataFrame


# select multiple columns
users[['age', 'gender']] # select two columns
my_cols = ['age', 'gender'] # or, create a list...
users[my_cols] # ...and use that list to select columns
type(users[my_cols]) # DataFrame

# %% row selection

df = users.copy()
df.iloc[0] # first row
df.iloc[0, 0] # first item of first row
df.iloc[0, 0] = 55

#row select (use ILOC)
for i in range(users.shape[0]):
    row = df.iloc[i]
    row.age *= 100 # setting a copy, and not the original frame data.
print(df) # df is not modified

#row edit (use LOC=>it accesses the INDEX of the row)
df = users.copy().reset_index(drop=True)
df.loc[0] # first row
df.loc[0, "age"] # first item of first row
df.loc[0, "age"] = 55
for i in range(df.shape[0]):
    df.loc[i, "age"] *= 10
print(df) # df is modified

# %% row filtering

users[users.age < 20] # only show users with age < 20
young_bool = users.age < 20 # or, create a Series of booleans...
young = users[young_bool] # ...and use that Series to filter rows
users[users.age < 20].job # select one column from the filtered results
print(young)

users[users.age < 20][['age', 'job']] # select multiple columns
users[(users.age > 20) & (users.gender == 'M')] # use multiple conditions
users[users.job.isin(['student', 'engineer'])] # filter specific values

# %% sorting

df = users.copy()
df.age.sort_values() # only works for a Series
df.sort_values(by='age') # sort rows by a specific column
df.sort_values(by='age', ascending=False) # use descending order instead
df.sort_values(by=['job', 'age']) # sort by multiple columns
df.sort_values(by=['job', 'age'], inplace=True) # modify df
print(df)

# %% describe a dataframe
#describe quantitative fields 
print(df.describe())

#describe all fields
print(df.describe(include='all'))

#describe the fields of a specific type of objects
print(df.describe(include=['object'])) # limit to one (or more) types

# aggregated statistics
print(df.groupby("job").mean())
print(df.groupby("job")["age"].mean())
print(df.groupby("job").describe(include='all'))

for grp, data in df.groupby("job"):
    print(grp, data)
    
# %% data cleaning - drop duplicates

df = users.append(df.iloc[0], ignore_index=True)
print(df.duplicated()) # Series of booleans

df.duplicated()# (True if a row is identical to a previous row)
df.duplicated().sum() # count of duplicates
df[df.duplicated()] # only show duplicates
df.age.duplicated() # check a single column for duplicates
df.duplicated(['age', 'gender']).sum() # specify columns for finding duplicates
df = df.drop_duplicates() # drop duplicate rows

# %% data cleaning - missing data

# Missing values are often just excluded
df = users.copy()
df.describe(include='all') # excludes missing values

# find missing values in a Series
df.height.isnull() # True if NaN, False otherwise
df.height.notnull() # False if NaN, True otherwise
df[df.height.notnull()] # only show rows where age is not NaN
df.height.isnull().sum() # count the missing values

# find missing values in a DataFrame
df.isnull() # DataFrame of booleans
df.isnull().sum() # calculate the sum of each column

# %% drop missing values
df.dropna() # drop a row if ANY values are missing
df.dropna(how='all') # drop a row only if ALL values are missing

# %% replace missing values 

df.height.mean()
df = users.copy()
df.loc[df.height.isnull(), "height"] = df["height"].mean()
print(df)


# %% outliers

size = pd.Series(np.random.normal(loc=175, size=20, scale=10))
# Corrupt the first 3 measures
size[:3] += 500

# %% strategy 1 use the mean
size_outlr_mean = size.copy()
size_outlr_mean[((size - size.mean()).abs() > 3 * size.std())] = size.mean()
print(size_outlr_mean.mean())

# %% use the median
mad = 1.4826 * np.median(np.abs(size - size.median()))
size_outlr_mad = size.copy()
size_outlr_mad[((size - size.median()).abs() > 3 * mad)] = size.median()
print(size_outlr_mad.mean(), size_outlr_mad.median())
# %% read from file

