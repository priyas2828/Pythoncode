# Am creating Object1 class to call this class in another file

class B:

    def __init__(self, a, b):
        print("This is second object constructor")
        c = a + b
        print(c)

    def sum(self, a, b):
        c = a + b
        print("The sum is " + str(c))

# Here We are not creating any object. But we are going create this object in another file
