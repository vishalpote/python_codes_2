n=int(input("Enter the number:"))
if n==1:
    print("Number is not prime..")
elif n>1:
    for i in range(2,n):
        if n%i==0:
            print("Number is not prime..")
            break
    else:
         print("Number is prime")
else:
    print("Number is not prime..")


# num=int(input("Enter the number:"))
# if num == 1:
#     print(num, "is not a prime number")
# elif num > 1:
#    # check for factors
#    for i in range(2,num):
#        if (num % i) == 0:
#            print(num,"is not a prime number")
#            print(i,"times",num//i,"is",num)
#            break
#    else:
#        print(num,"is a prime number")
       
# # if input number is less than
# # or equal to 1, it is not prime
# else:
#    print(num,"is not a prime number")