n=int(input("Enter : "))
rev=0
x=0;
while n!=0:
     x=n%10
     n=n//10
     rev=rev*10+x
print(rev)
