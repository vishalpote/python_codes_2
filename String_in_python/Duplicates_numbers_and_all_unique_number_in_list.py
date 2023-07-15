n=int(input("Enter the number:"))
l=[]
for i in range(n):
    l.append(input("Enter the Element:"))
# print(l)
# for j in range(len(l)-1):
#     for k in range(j):
#         if l[k]==l[k]:
#             print("Duplicates")
#         else:
#             print("All_unique")

print(l)
for j in range(len(l)-1):
    if l[j]==l[j+1]:
        print("duplicates")
    else:
        print("all unique")
        break