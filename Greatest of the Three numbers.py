n1=int(input("Enter 1st number\t"))
n2=int(input("Enter 2nd number\t"))
n3=int(input("Enter 3rd number\t"))
if n1>n2 and n1>n3:
    print(n1,"is greatest")
elif n2>n3:
    print(n2,"is greatest")
elif n1==n2==n3:
    print("All are equal")
else:
    print(n3,"is greatest")
