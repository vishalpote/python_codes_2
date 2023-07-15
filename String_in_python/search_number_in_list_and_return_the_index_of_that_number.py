l=[]
n=int(input("How many Element:"))
for i in range(n+1):
    l.append(input("Enter the element:"))
print(l)
x=int(input("Enter the element you want to searched:"))
if x not in l:
        print("The number is not in the List")
print(l[x])