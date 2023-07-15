def rang(start,end,n):
    l=[]
    for i in range(start,end):
            l.append(i)
            if n==i:
                print("number are in range")
            else:
                print("number is not in range")
rang(1,20,n=int(input("enter the number to find:")))