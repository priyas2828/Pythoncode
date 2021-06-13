class A:
    # Creating a construction with keyword __init()__
    def __init__(self):
        print("This is constructor with keyword init")

    # Constructor with argument
    def __int__(self, a, b):
        c = a + b
        return c    # Its never returns any value if you try to run it will throw error
        # print("The value of c is " + str(c))

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


obj = A() # creating objection of class
obj.hello() # with object reference calling the constructor method
obj.sum(12, 13)
x = obj.mul(2, 3)
print(x)
obj.__int__(12, 13)
obj.__init__()

