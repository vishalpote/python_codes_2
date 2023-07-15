# s=input("Enter the string:")
# if(s==s[::-1]):
#     print("Palindrom string..")
# else:
#     print("Not palindrom string..")



#another method

s=input("Enter the string:")
x=""
for i in s:
    x=i+x
print("Palindrom string" if x==s else "not palindrom")
# if(x==s):
#     print("Palindrom")
# else:
#     print("Not palindrom")