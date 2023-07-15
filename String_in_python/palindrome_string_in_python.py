# s=input("Enter the string: ")
# print("String is palindrom" if s==s[::-1] else "the string is not palindrome")




#other method using the loop

# s=input("Enter the string:")
# for i in range(0,int(len(s)/2)):
#     if s[i]!=s[len(s)-i-1]:
#         print("String is not palindrome")
#         break
# else:
#     print("string is palindrome")



#other methods

s=input("enter the string:")
x=""
for i in s:
    x=i+x
if(x==s):
    print("palindrom")
else:
    print("not palindrome")