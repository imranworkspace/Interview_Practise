my_array = [8, 12, 9,7, 2, 4, 11, 7,2]
minVal=my_array[0] 
[minVal:=i  if i<minVal else minVal for i in my_array]
print(minVal)