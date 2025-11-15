class Student:
    def hello(self):
        print('hello student')

# define function outside the class
def money(self):
    return 'I am patched'

# monkey-patching
Student.hello = money

s = Student()
print(s.hello())
