# emailAddress = "Testingworldindia@gmail.com"
# a = "gmail"
# Find a string in to another string
# print(emailAddress.find(a))

# Split string on behalf of splitter
emailAddress = "This is my email id Testingworldindia@gmail.com"
list1 = emailAddress.split(" ")
# print(len(list1))
# print(list1)

# Checking how many times "is" is available in given string
z = 0
for i in list1:
    if i == "is":
        z += 1
        #print("Found")
print(z)
