emailAddress = "Testingworldindia@gmail.com"
# Replace a part of string
print(emailAddress.replace("gmail", "yahoo"))

# Find how many l exist in your string
#z = 0  # How many times l is exist
#for i in emailAddress:
#   if(i=='l'):
#       z += 1
        #print("Yes Found")
#print(z)

# how may l in he string and need not to go for a loop
x=len(emailAddress) # total 27
y=len(emailAddress.replace("l", "")) # total 25

print(x-y)
