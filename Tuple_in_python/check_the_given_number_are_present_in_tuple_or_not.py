l=[i for i in range(15)]
t=tuple(l)
print("****************tuple********************")
print(t)
x=int(input("find the element you want:"))
if x in t:
    print("number are present in tuple")
else:
    print("the number are not present into the tuple")