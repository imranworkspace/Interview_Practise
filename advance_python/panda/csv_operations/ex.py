import pandas as pd
import numpy  as np

dic1={
    "name":["imran","irfan","afreen","zun"],
    "marks":[75,85,48,98],
    "city":["latur","pune","mumbai","latur"]
}

df = pd.DataFrame(dic1)
print(df)

myfile = df.to_csv("stud.csv")
myfile = df.to_csv("stud.csv",index=False)
# create one dimention series with index
ser=pd.Series(np.random.rand(34))
print(ser)
print(type(ser))


newdf = pd.DataFrame(np.random.rand(334,5),np.arange(334))
# show first 5 rows
print(newdf.head())
print(type(newdf))
# show min std 75% 50% etc.
print(newdf.describe())
# check data type of dataframe or series
print(newdf.dtypes)

print()
print()
# newdf[0][0]="imran"
print(newdf)
# see indexes 334 
print(newdf.index)
# see columns 5
print(newdf.columns)
# convert colum to row and row to column
print(newdf.T)
# sort index desending axis for 0 for row, 1 for column
# print(newdf.sort_index(axis=0,ascending=False))
print(newdf.sort_index(axis=1,ascending=False))
# print series or column 
print(newdf[0])
print(type(newdf[0]))
# copy one df to another using copy() function
newdf2=newdf.copy()
newdf2[0][0]=95825
print(newdf)
print(newdf2)
# use of loc function to change column name
newdf2.columns=list("ABCDE")
print(newdf2)
# change value using column name
newdf2.loc[0,'A']=454587
print(newdf2.head(2))
# remove column we use drop() with axis=1
# newdf2.drop(0,axis=1)
print(newdf2)