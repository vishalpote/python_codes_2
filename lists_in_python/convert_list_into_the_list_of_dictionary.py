value_list=['vishal',21,'sager',22]
key_list=['name','age']
l=[]
for i in range(0,len(value_list),2):
    l.append({key_list[0]:value_list[i],key_list[1]:value_list[i+1]})
print(l)
