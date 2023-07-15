n=int(input("Enter the number:"))
count=0
if(n==0 and n==1):
    print("Number is Not Prime")
for i in range(2,n):
    if (n%i)==0:
        count+=1
if(count==0):
    print("Number is prime ")
else:
    print("number is not prime")