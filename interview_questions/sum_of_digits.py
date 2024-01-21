def sum_of_digit(n):
    sum=0
    for i in str(n):
        sum+=int(i)
    return sum
n=12345
print(sum_of_digit(n))