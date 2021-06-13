# (4*20)+10

def multiply(a, b):
    c = a * b
    return c  # Return ing the value use the keyword return


def add(a, b):
    c = a + b
    print(c)


x = multiply(4, 20)
add(x, 10)


# Functions no arg but return a value
def retData():
    a = 100
    return a

x = retData()
print(x)
