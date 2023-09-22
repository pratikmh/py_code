from unittest import skip


n=int(input("enter no "))
m=n
total=0
for i in range(1,n):
    if n%i==0:
        print(i)
        total=total+i
print(total)
if total==m:
    print("perfect number")
else:
    print("not perfect number")

    