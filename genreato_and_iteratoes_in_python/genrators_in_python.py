def genrator():
    for i in range(100):
        yield i
gen=genrator()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

# for j in gen:
#     print(j)


l=[i for i in range(10000000)]
import sys
print(sys.getsizeof(l))
print(sys.getsizeof(gen))