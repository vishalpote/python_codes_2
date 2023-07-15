#first way to find length

l=[i for i in range(11)]
print(len(l))


#second way to find the length of the list


l2=[i for i in range(5)]
count=0
for j in range(len(l2)):
    count+=1
print(count)


#third way to find length of list
l3=[i for i in range(50)]
c=0
for k in l3:
    c+=1
print(c)