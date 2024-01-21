from array import array
num_arr = array('i',[1,2,3,4,4,5])
print(num_arr)
print(type(num_arr))

num_arr.append(6)
print(num_arr)

num_arr.pop()
print(num_arr)

in_ = num_arr.index(4)
print(in_)