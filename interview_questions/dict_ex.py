new_list = [(5, 'a'), (2, 'b'), (3, 'c'), (5, 'ab')]

key_dict={}
for key,value in new_list:
    if key not in key_dict:
        key_dict[key]=[value]
    else:
        key_dict[key].append(value)
print(key_dict)
