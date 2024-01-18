dict1 = {1: 'imran', 2: 'irfan', 3: 'afreen'}
dict_2 = {4: 'imran', 5: 'irfan', 5: 'afreen'}
dict_3=dict1.copy()
dict_3.update(dict_2)
print(dict_3)