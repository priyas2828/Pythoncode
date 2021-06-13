
# take number form the user

number=input("Please enter the number : ")
for i in range(1, 11):
    if(int(number)*i%10==0):
        continue # it will skip the multiply of 5( 30 and 60 )wont execute
    print(int(number)*i)

