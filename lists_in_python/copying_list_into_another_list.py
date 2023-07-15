#first way to copy list

l1=[i for i in range(10)]
print("***********original*************")
print(l1)
print("***********copying*******************")
l2=l1.copy()
print(l2)


#second way to copied list into another list


l3=[i for i in range(10)]
print("********original**************")
print(l3)
print("*********copied*************")
l4=[]
for j in range(len(l3)):
    l4.append(j)
print(l4)