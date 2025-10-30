class A:
    def hello(self):
        print("Hello from class A")

class B(A):
    def hello(self):
        super().hello()  # Calls the 'hello' method from class A
        print("Hello from class B")


# Create an instance of D
b = B()
b.hello()
