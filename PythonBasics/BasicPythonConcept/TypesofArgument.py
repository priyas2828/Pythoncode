# Required Arguments
def takeInput(a, b):
    c = a + b
    print("Sum of Values " + str(c))

# Keyword Arguments
def takeMyInput(a, b):
    c = a + b
    print("Sum of Values " + str(c))

# Default Argument- It must be defined always at the end
def takedefArgument(a, b=10):
    c = a+ b
    print("The value is  "+ str(c))

takedefArgument(a= 100)
takeInput(10, 20)
takeMyInput(b=100, a=200)

