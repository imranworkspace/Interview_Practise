def myfun(lst):
    d=dict()
    for index,item in enumerate(lst,start=0):
        if isinstance(item,list):
            d[index]=myfun(item)
        else:
            d[index]=item
    return d 
    
lst = ['a','b',['e','f'],'g',['h']]
# expected from above list 
# dict = {0:'a',1:'b',2:{0:'e',1:'f'},3:'g',4:{0:'h'}}

print(myfun(lst))