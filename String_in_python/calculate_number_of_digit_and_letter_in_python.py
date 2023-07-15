s=input("Enter the string:")
cd=0
cl=0
for i in range(len(s)-1):
    if s.isalpha:
        cl+=1
    elif s.isnumeric:
        cd+=1
print("number of digit:",cd)
print("number of letter:",cl)
