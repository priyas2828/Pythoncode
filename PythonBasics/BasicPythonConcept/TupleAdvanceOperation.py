tuple1 = (23, 45.6, "Testing", 34, 79, 97, 23)
tuple2 = (100,200)
# how many time the value displayed in tuple
# Count no of times the value displayed in tuple
print(tuple1.count(23))

# find index of any value in tuple
print(tuple1.index(34))

# Merge two tuples
tuple3 = tuple1 + tuple2
print(tuple3)

# Display all the values of the tuple
#for i in tuple1:
#    print(i)

# another way
i = len(tuple1)
for i in range(0, 4):
    print(tuple1[i])