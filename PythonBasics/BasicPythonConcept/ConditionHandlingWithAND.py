# If the number is positive divisible by 2  then it should print valid number

inputNum=input("Please enter the number -")
inputNum=int(inputNum)

if(inputNum>=0 and inputNum%2==0):  # AND means both the condition must be true
    print("This is Valid number")
else:
    print("This is Invalid number")