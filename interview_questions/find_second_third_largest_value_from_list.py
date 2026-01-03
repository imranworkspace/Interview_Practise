nums = [10, 5, 20, 8,100,40,50,60,80]
first=second=third=nums[0]
for n in nums:
    if n>first:
        third=second
        second=first
        first=n
    elif n<first and n>second:
        third=second
        second=n
    elif n<second and n>third:
        third=n
print(second)
print(third)
    