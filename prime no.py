num=int(input("enter the no"))
j=0
for i in range(num):
    if i==0 or i==1:
        continue
    elif num%i==0:
        j=j+1
if j>0:
    print(num,"is not prime")
else:
    print(num,'is prime')
