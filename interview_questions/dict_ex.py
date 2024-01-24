def list_to_dict(new_list):
    d=dict()
    for key,value in new_list:
        if key not in new_list:
            d[key]=value
        else:
            d[key]=value
    return d

new_list = [(5, 'a'), (2, 'b'), (3, 'c'), (5, 'ab')]
print(list_to_dict(new_list))
