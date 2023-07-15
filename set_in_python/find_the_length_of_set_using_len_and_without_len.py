
#this is the in-build-function
# s={
# i for i in range(1,16)
# }
# print(len(s))


#other method without using built in function
s={i for i in range(1,11)}
count=0;
for i in s:
    count+=1
print(count)