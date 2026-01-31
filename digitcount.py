n=int(input("Enter number : "))
c=0
while n>0:
    rem=n%10
    c+=1
    n//=10

print(c)
