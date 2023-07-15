s=int(input("Enter the starting point:"))
e=int(input("Enter the Ending point:"))
for i in range(s,e+1):
    temp=i
    sum=0
    while temp!=0:
        r=temp%10
        sum+=r**len(str(i))
        temp//=10
# print("Number is armstrong" if i==sum else "Number is not armstrong")
    if i==sum:
            print(i)