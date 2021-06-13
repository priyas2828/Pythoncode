# Declaring a varilable
# z=7
# for i in range(1,11):
#    print(str(z) + " * " + str(i) + "=" +str(z*i)) # Converting all interger to string i.e type casting

# Taking input for user
# whetver the input form the user convert to integer


number = input("Please enter the number : ")

for i in range(2, 11):
    print(number + " * " + str(i) + " = " + str(int(number) * i))
