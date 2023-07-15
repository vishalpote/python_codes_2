#first way to reverse the list


l=[i for i in range(10)]
print("original list:")
print(l)
print("after reversing the list:")
print(l[::-1])


#second  way to reverse the list

l2=[i for i in range(10)]
print("original list:")
print(l2)
print("after reversing the list:")
l2.reverse()
print(l2)


#third ways to reverse the list

l3=[i for i in range(15)]
print("original list:")
print(l3)
print("after reversing the list:")
print(list(reversed(l3)))


#fourth way to reverse the list

def revrse(l):
    left=0
    right=len(l)-1
    print("*******original********")
    print(l)
    while(left<right):
        temp=l[left]
        l[left]=l[right]
        l[right]=temp
        left+=1
        right-=1
 
    print("*********reversed*************")
    return l
print(revrse(l=[i for i in range(11)]))