lst=[1,2,3,4,5,7,8]
n=len(lst)+1
exp_=n*(n+1)//2
print(exp_)
act_sum=sum(lst)
print(act_sum)
result=exp_-act_sum
print(result)