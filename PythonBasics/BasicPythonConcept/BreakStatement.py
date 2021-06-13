
# syntax
#for i in range(1,10):
#    if(i==5):
#        break # when its check on 5 it will break the loop and come out of the loop
#    print(i)

# Take number form user
number=input("Please enter the number :" )
for i in range(1, 11):
    if(int(number)*i==60):
        break
    print(int(number)*i)
