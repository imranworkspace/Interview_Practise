def list_to_dict(new_list):
    d={}
    for k,v in new_list:
        if k not in new_list:
            d[k]=v
        else:
            d[k]=v
    return d
    
# new_list = [(5, 'a'), (2, 'b'), (3, 'c')]
new_list = [(5, 'a'), (2, 'b'), (3, 'c'), (5, 'ab')]
print(list_to_dict(new_list))