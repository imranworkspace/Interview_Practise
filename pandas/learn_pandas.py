import pandas as pd


'''file reading from csv to dataframe '''
# df = pd.read_csv("data.csv")
# # print(df)
# print(df.to_string())


print(pd.__version__)

'''custome dataset'''
# mydataset={
#     "name":["imran","zunaisha","afreen"],
#     "ages":[33,2,29],
#     "hobbies":['cricket',"football","swimming"]
# }

# df = pd.DataFrame(mydataset)
# print(df.to_string())


'''series'''
# something like column, one dimention array
# ages=[33,2,29]
# names=["imran","zunaisha","afreen"]
# df_ages = pd.Series(ages)
# df_names = pd.Series(names)
# print(df_ages)
# print(ages[1]) # required index
# print(df_names)
# print(names[2])

'''series with indexing - list type of data '''

# names=["IMRAN","IQBAL","SHAIKH"]
# df_names = pd.Series(names,index=['Fname','Mname','Lname'])
# print(df_names)
# print(df_names["Mname"])

'''series with indexing - dict type of data '''
# calegories = {"day1":440,"day2":400,"day3":350}
# df = pd.Series(calegories,index=['day1','day2','day3'])
# print(df)
# print(df["day2"])

''''''
context = {"calerogies":[450,420,380],
           "duration":[30,40,50]}
df = pd.DataFrame(context)
print(df)
print(df.loc[0])
input()
print(df.loc[[0,1]])
print('---')
df = pd.DataFrame(context,index=["day1","day2","day3"])
print(df)
print(df.loc['day3'])