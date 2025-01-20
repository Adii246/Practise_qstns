
num=int(input("enter the number:"))
n=num
sum= 0
while n>0:
    rem=n%10
    sum=(sum*10)+rem
    n=int(n/10)
rnum=sum
if num==rnum:
    print("palindorme")
else:
    print("not palindrome")
