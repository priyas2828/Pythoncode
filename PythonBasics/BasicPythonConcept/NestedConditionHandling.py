
# Take 1 number from the user


inputNum=input("Please enter the number")
inputNum=int(inputNum)

if(inputNum>=0):
    if(inputNum%2==0): # This is nested
        print("This is even number")
    else:
        print("This is odd number")
else:
    print("This is negative number")
