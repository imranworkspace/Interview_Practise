def rev(lst):
    if len(lst)==0:
        return []
    return [lst[-1]]+rev(lst[:-1])

lst=[1,2,3]
print(rev(lst))