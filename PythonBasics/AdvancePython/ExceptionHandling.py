
# Read two input from the user
# We are going to display the error
# Once your un the code we will get a error saying ValueError: invalid literal for int() with base 10: '123dr.
# So handle the error we going to use exception saying please enter only the number not alphanumeric
# Refer the "Handle exception.py" code like how to handle the exception

user_input1= input("Please enter first number")
user_Input2=input("Enter second number")
c= int(user_input1) + int(user_Input2)
print(c)
