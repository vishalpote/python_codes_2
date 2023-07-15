s=int(input("enter the starting point:"))
e=int(input("enter the ending point:"))
a=0
b=1
print(a)
print(b)
for i in range(s,e):
    c=a+b
    print(c)
    a=b
    b=c
