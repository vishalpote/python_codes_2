l=[['a','b',1,2],['c','d',3,4]]
d={(i[0],i[1]):tuple(i[2:]) for i in l}
print(d)