def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)
x=int(input("How many Terms you want:"))
if x<=0:
    print("please enetr positive number..")
else:
    for i in range(x):
        print(fib(i))