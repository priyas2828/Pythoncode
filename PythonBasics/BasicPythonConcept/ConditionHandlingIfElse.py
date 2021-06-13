

# checking the number is greater than 100 then  print "GREATER"
# : means body of the if is started
# Else i need to dispaly the number is small
#i=10
#if(i>100):
#    print("Number is Greater")
#else:
#    print("Number is small")

# Take numbers from user and print if its greater or not
# We got error saying > symbol is not support on int or str.
# What ever the data it comes from the user is always string hence we converting to int
# We are typecasting to > symbol is string hence we are converting to int which is type casting

input1=input("Please enter the data--")
if int(input1)>100:
    print("The Value is greater")
else:
    print("the number is smaller")




