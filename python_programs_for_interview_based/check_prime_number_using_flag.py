n=int(input("eEnter the number:"))
flag=False
if n==1:
    print("Number is not prime")
elif n>1:
    for i in range(2,n):
        if n%i==0:
            flag=True
            break
    if flag==True:
        print("number is not prime")
    else:
        print("Number is prime")