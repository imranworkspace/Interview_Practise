
# syntax: lambda arguments:expression

cube = lambda a:a*a*a
print(cube(2))

add = lambda a,b,c,d,e,f,g,h,i:a+b+c+d+e+f+g+h+i
print(add(1,2,3,4,5,6,7,8,9))

lst_ = [1,2,3,4,5,6,7,8,9,10]      
evn_num=list(filter(lambda num:num%2==0 and num%3==0,lst_))
print(evn_num)

fruits = ['apple','banana','apriot']
filter_obj = list(filter(lambda s:s[0]=='a',fruits))
map_obj = list(map(lambda s:s[0]=='a',fruits))
print(map_obj)
print(filter_obj)

