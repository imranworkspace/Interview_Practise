def rev_lst(lst):
    if not lst:
        return []
    else:
        print(lst[-1])
        input()
        print(lst[:-1])
        input()
        return [lst[-1]] + rev_lst(lst[:-1])
lst=[3,2,1]
print(rev_lst(lst))