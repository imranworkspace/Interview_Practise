name = "geekyshows"
print(name)
print(name[0])
print(name[1])
print(name[2])
print()
print(name[-1])
print(name[-2])
print(name[-3])

print('without index')
for s in name:
    print(s)
print()
print('with index')
for i in range(len(name)):
    print(name[i])
print()
print(len(name))

print("Repetition()")
print("$"*7)

name=" imran "
print(name * 3)