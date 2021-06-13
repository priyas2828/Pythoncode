# Here in TC1.py we are going to use common module.py
# This is called import statement
import ProjectStructure.Library.CommonModule  # To import take directory name.sub directory and python file name

objA = ProjectStructure.Library.CommonModule.A()  # Create object of class A
objA.startBrowserA()

objB = ProjectStructure.Library.CommonModule.B()  # Create object of class B
objB.startBrowserB()

# From module import class and import A  is we need to provide a class name
from ProjectStructure.Library.CommonModule import A # From import we need to provide which exact class we need to import

objA = A() # If we use from method, We don't required to provide the directory name while creating the object. You can
# call directly
objA.startBrowserA()
