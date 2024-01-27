# exptedted {'name': 'Kelly', 'salary': 8000}

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]
#------------------------------------------------------------
#using dic comprehention
# d_com = {k : sample_dict[k] for k in keys}
# print(d_com)
#------------------------------------------------------------
# using update function
res = {}
for k in keys:
    res.update({k : sample_dict[k]})
print(res)
#------------------------------------------------------------