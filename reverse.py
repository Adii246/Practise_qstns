num=int(input("enter the number:"))
sum= 0
while num>0:
    rem=num%10
    sum=(sum*10)+rem
    num=int(num/10)
rnum=sum
print(f"Reverse is {rnum}")
