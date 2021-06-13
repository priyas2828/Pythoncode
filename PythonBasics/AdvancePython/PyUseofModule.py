
# Whenever we are importing any module, that module executable code will run automatically
import Pymodule

# We are calling module functions by using module name

X = Pymodule.sum(10, 20)  # Value returning from C will be storing it in x and print the value
print(X)

# Now are gonna see class inside the module
# We need to create object of class return in any module
obj = Pymodule.A()  # Whenever you are calling object of class use modules name.class name
obj.testing()
