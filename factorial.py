num=int(input('enter the number'))
l=1
for i in range(num+1):
    if i==0:
        continue
    l*=i
print(l)
