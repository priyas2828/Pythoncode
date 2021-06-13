
# if the number is less than 0 or greater than 100 in both cases I need to dispaly its an invalid number


inputNum=input("Please enter the number -")
inputNum=int(inputNum)

if(inputNum>100 or inputNum<0):
    print("This is invalid number")
else:
    print("This is Valid number")