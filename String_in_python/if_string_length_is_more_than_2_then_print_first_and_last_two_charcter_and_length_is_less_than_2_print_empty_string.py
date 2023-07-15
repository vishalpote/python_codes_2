x=input("Enter the string:")
if(len(x)<2):
    print("Empty string")
else:
    print(x[0:2],x[len(x)-2:])