def sum1(n):
   if n<=1:
      return n
   else:
      return n*sum1(n-1)
print(sum1(n=int(input("enter the number:"))))       
    