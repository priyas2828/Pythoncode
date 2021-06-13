class A:
    # Functions with no argument and no return value
    def hello(self):
        print("Hello World")

    # Function which will take two argument sum value and display it
    def sum(self, a, b):
        c = a + b
        print("The sum is " + str(c))
    # Function take argument and return the value as well
    def mul(self, a, b):
        c = a * b
        return c  # Whatever the value is coming back save it in one variable

obj = A()
obj.hello()
obj.sum(12, 13)
x = obj.mul(2, 3)
print(x)
