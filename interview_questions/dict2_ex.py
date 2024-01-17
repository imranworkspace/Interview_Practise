lst = ['a','b',['e','f'],'g',['h']]
# expected from above list 
# dict = {0:'a',1:'b',2:{0:'e',1:'f'},3:'g',4:{0:'h'}}

# diff between stateless and statefull example in python

def list_to_dict(lst):
    result_dict = {}

    for i, item in enumerate(lst):
        if isinstance(item, list):
            result_dict[i] = list_to_dict(item)
        else:
            result_dict[i] = item

    return result_dict

lst = ['a', 'b', ['e', 'f'], 'g', ['h']]
result_dict = list_to_dict(lst)

print(result_dict)
