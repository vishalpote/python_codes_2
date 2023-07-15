l1=[1,2,4,3,1,5,6]
l2=[]
count=0
for i in l1:
    if i not in l2:
        count+=1
        l2.append(i)
print(count)