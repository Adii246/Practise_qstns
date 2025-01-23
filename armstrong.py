num=(input("ENTER THE NUMBER"))
p=0
length=len(num)
num=int(num)
number=num
for i in range(num):
    d=num%10
    n=d*d
    p+=n
if number==p:
    print(number,'is armstrong')
else:
    print(number,'is not armstrong')
