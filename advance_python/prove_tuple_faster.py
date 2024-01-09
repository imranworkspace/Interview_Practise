import timeit

lst=[i for i in range(1000000)]
mytup = tuple(lst)

lst_time = timeit.timeit(lambda:lst[500000],number=10000)
tup_time = timeit.timeit(lambda:mytup[500000],number=10000)

print('list time ',lst_time)
print('tup time  ',tup_time)