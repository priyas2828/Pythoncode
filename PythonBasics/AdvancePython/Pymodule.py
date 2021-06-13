# This is Python Module
# Here we are writing executable code

print("Welcome to python module with  name - PyModule.py")

# Functions inside python file(Without class), Module Functions

def testingPythonModuleFunction():
    print("This is Python module Function")


def sum(a, b): # We are gonna call this function in Pyuseofmodule.py file
    c = a + b
    return c


class A:
    # inside class we can create Constructor also
    def __init__(self):
        print("This is Constructor")

    def testing(self):
        print("This is My class Function")
