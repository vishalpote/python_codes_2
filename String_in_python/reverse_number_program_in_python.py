n=int(input("Enter the number:"))
r=0;
while n!=0:
    r=r*10+(n%10)
    n//=10
print("The Reverse number is:",r)