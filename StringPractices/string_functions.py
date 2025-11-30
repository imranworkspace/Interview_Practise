name="imraN"
print(name.lower())
print(name.upper())
print(name.swapcase()) # convert if upper then convert into lower
name="imran ikbal shaikh"
print(name.title()) ## first char in upper case into string 
print()

print('isupper,islower,istitle')
str1="Imran786"
print(str1.isupper())
print(str1.islower())
print(str1.istitle())
print()
print('isdigit,isalpha,isalnum')
str1="imran786ok hello"
print("123".isdigit())
print("Imran123".isalnum())
print("imran".isalpha())# atleast one alpha numeric then return true
print(" ".isspace())#
print(" imran".lstrip())#
print(" imran ".rstrip())#
print(" imran ".strip())
print("my name is imran".replace("imran","irfan"))
print("my name is imran".split()) 

# isdigit,isalpha,isalnum
# True
# True
# True
# True
# imran
#  imran
# imran
# my name is irfan
# ['my', 'name', 'is', 'imran']

print("how-are-you".split('-'))
str3=('how','are','you')
print(".".join(str3))
# ['how', 'are', 'you']
# how.are.you

print()
print("imran".startswith("i"))
print("imran".endswith("x"))
# True
# False
