n=int(input("how many element you want to add in tuple:"))
l=[]
for i in range(n):
    l.append(input("add element into the tuple:"))
t=tuple(l)
print(t)