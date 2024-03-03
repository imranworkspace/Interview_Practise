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