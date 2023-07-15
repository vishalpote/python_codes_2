s1={i for i in range(1,15)}
s2={i for i in range(5,25)}
print(s1)
print(s2)
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.symmetric_difference(s2))
print(s1.difference(s2))
print(s1.issubset(s2))
print(s1.issuperset(s2))

