# start=int(input("Enter starting point:"))
# end=int(input("Enter ending point:"))
def fabonacci(n):
    if n<=1:
        return n
    else:
        return fabonacci(n-1)+fabonacci(n-2)
nt=int(input("Enter how many term:"))
if nt<=0:
    print("please enter positive terms:")
else:
    for i in range(nt):
        print(fabonacci(i))