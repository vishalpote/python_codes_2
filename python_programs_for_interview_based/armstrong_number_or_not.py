import math
n=int(input("Enter the number:"))
s=len(str(n))
sum=0
x=n
while x!=0:
    r=x%10
    sum=sum+r**(len(str(n)))
    x=x//10
if(n==sum):
    print("Armstrong number")
else:
    print("Not Armstrong number")