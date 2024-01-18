# Exercise 4: Initialize dictionary with default values
# expected : {'Kelly': {'designation': 'Developer', 'salary': 8000}, 'Emma': {'designation': 'Developer', 'salary': 8000}}
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

gval=dict.fromkeys(employees,defaults)
print(gval)
print(gval['Kelly'])