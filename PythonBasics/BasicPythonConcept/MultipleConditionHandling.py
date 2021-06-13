# Taking 1 Input
# Check number is negative-Display Negative number-check if its 0 then 0
# If number is Positive then its an even number or odd number

inputNum = input("Please enter your number -")
inputNum = int(inputNum)
if (inputNum < 0):
    print("The negative numbers ")

elif inputNum == 0:
    print("The number is Zero")

elif (inputNum % 2 == 0):
    print("This is even number ")
else:
    print("This is odd number ")
