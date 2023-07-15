l=[1,4,2,1,3,6,2]
print(l)
count1=0
x=int(input("Enter the element you want to count:"))
for i in l:
    if i==x:
        count1+=1
print(x,"occurs in",count1,"times")