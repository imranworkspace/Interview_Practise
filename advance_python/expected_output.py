

#######################################################################################
# expected my name is imran
l1=['my','is']
l2=['name','imran']
lst_cmp = [x+' '+y for x,y in zip(l1,l2)]
mystr=''
for i in lst_cmp:
    mystr=mystr+i+' '
print(mystr)

#######################################################################################
# expected python good language
lst=[
    [1,2,'python'],
    [3,4,'is','good',5],
    ['language',5,7]
    ]
lst_cmp = [[lst[0][2], lst[1][2],lst[1][3],lst[2][0]] for i in lst]
x=lst_cmp[0]
mystr = ''
for i in x:
    mystr=mystr+i+' '
print(mystr)
# x = str(lst[0][2]) +' '+ str(lst[1][2]) +' '+ str(lst[2][0])
# print(x)
#######################################################################################

    # expected [1,2,3,4,5,6]
    # lst1=[1,2,3,4,3]
    # lst2=[4,5,6]
# print(list(set(lst1) ^ set(lst2)))

#######################################################################################

# expected [1,2,3,4,5,6]
# lst=[1,2,3,4,5,6,1,4,3,2]
# print(list(set(lst)))








# palindrome using reverse fun
# def pali(name):
#     rev=''.join(reversed(name))
#     if rev==name:
#         print(f'{name} is palindrome')
#     else:
#         print('not palindrome')
        
# name=input('enter name :-> ')
# pali(name)




# palindrome withou reverse fun
# def pali(name):
#     return name==name[::-1]
    
# name=input('enter name :-> ')
# res=pali(name)

# if res:
#     print(f'{name} is palindrome ')
# else:
#     print('not palindrome')




# fibonacci series
# def fibo(n):
#     count,n1,n2=0,0,1
#     while count<=n:
#         print(n1)
#         temp=n1+n2
#         n1=n2
#         n2=temp
#         count+=1
# n=int(input('enter number  '))
# fibo(n)