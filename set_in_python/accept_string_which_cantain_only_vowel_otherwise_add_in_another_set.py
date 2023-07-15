s=input("Enter the string:")
s1=set()
s2=set()
if ((s=='a' and s=='e' and s=='i' and s=='o' and s=='u') or (s=='A' and s=='E' and s=='I' and s=='O' and s=='U')):
    s1.add(s)
    print(s1)
else:
    s2.add(s)
    print(s2)