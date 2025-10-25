# syntax of enumerate=(sequence,start)
# sequence :-> list,tuple,string
# start :-> 0(default),1 and so on

print('emumerates list')
fruits = ['apple', 'orange', 'banana']
# Use enumerate with a custom starting index (incremented by 2)
for index, fruit in enumerate(fruits, start=1):  # Change the starting value as needed
    print(f"Index {index*3}: {fruit}")


print('emumerates string')
name='imran'    
for index,val in enumerate(name,start=1):
    print(f'{index*4} of {val}')