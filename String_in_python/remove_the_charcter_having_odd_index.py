s=input("Enter the string:")
x=""
for i in range(len(s)):
     if i%2==0:
            x=x+s[i]
print(x)