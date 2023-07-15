def prime(n):
    if(n==0 and n==1):
        print("number is not prime")
    count=0
    for i in range(2,n):
        if(n%i==0):
            count+=1
    # if(count==0):
    #     print("prime")
    # else:
    #     print("not prime")
    print("number is prime" if count==0 else "number is not prime")
prime(n=int(input("Enter the number:")))