dict1 = {1: 'imran', 2: 'irfan', 3: 'afreen'}
dict_2 = {4: 'imran', 5: 'irfan', 5: 'afreen'}
dict_3 = {**dict1, **dict_2}
print(dict_3)