# first way to clear a list

l=[i for i in range(10)]
print(l)
l.clear()
print(l)

#second way to clear a list

l2=[i for i in range(5)]
print(l2)
del l2[:]
print(l2)