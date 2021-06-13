# Here we are going to see try, exception and finally exception
# try means this code can throw exception
# If we are getting error in try block code will jump in to an exception
# If you use try its mandatory to use exception and vice versa
# Finally is always place after the try and except
# Finally is not mandatory . even if its throw exception or not fainally will be execute at the end

try:
    user_input1 = input("Please enter first number")
    user_Input2 = input("Enter second number")
    c = int(user_input1) + int(user_Input2) # typecasting the value
    print(c)

except: # this is execute only in case of exception
    print("This is your input is incorrect please enter the correct data")
finally:
    print("This code I want to execute always at the end")

