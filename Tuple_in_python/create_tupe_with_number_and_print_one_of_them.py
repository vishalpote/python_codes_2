l=[]
n=int(input("enter the number:"))
for i in range(n):
    l.append(input("enter the element:"))
t=tuple(l)
print(t)
print(t[2])