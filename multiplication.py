t=int(input("Enter no. of testcases: "))
print("Multiplication table: ")
for i in range(t):
    n=int(input("Enter number: "))
    for j in range(1,11):
        print(n,"*",j,"=",n*j)

