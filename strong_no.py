# 1! + 4! + 5!=145  so its strong no
n=int(input("enter no"))
total=0
m=n
while n>0:
    fact=1
    rem=int(n%10)
    for i in range(1,rem+1):
        fact=fact*i
    # print(fact)
    n=n//10
    total=total+fact
if total==m:
    print("strong no")
else:
    print("not strong no")
