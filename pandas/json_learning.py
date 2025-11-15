import pandas as pd

df = pd.read_json("data.json")
print(df)
print(df.head(5))# top 5
print(df.head(-5)) # minus-5 from df
print(df.tail()) # last 5

input()
print(df.info())