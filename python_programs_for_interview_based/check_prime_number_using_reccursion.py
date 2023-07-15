def prime(n,i=2):
    if n<=2:
        if n==2:
            return True
        else:
            return False
    if n%i==0:
        return False
    if i*i>n:
        return True
    return prime(n,i+1)
x=int(input("Enter number:"))
if(prime(x)):
    print("Is prime")
else:
    print("Is not prime")