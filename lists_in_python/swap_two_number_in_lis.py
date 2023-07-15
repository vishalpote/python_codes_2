def swaping(l):
    print("**************the lists***************")
    print(l)
    print("***********after swaping****************")
    l[0],l[3]=l[3],l[0]
    return l
print(swaping( l=[i for i in range(11)]))

