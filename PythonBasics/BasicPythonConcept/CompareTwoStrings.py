# Basicsc
#a="Testing"
#b="testing"
#if (a==b):
#if(a.strip()==b.strip()):
#    print("Compared")
#else:
#    print("Not Compared")
#if(a.upper()==b.upper()):
#    print("same")
#else:
#    print("not same")

# Reverse a string and check palindrome
a = "Testing"
b = ""
l=len(a) # legth should start form 0
#print(l)
for i in range((l-1), -1, -1): # l-1 is totallength -1 and -1 is excluding the last value  and -1 is decreasing by 1
# print(a[i])
    b = b+a[i]
print(b)

# Palindrome- reverse the word
if(a==b):
    print("this is palindrome")
else:
    print("Not Palindrome")


