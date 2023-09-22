n=int(input("enter no "))
num=n
rev=0
for i in str(n):
    rem=n%10
    rev=(rev*10)+rem
    n=n//10
if (num==rev):
    print("no is pallindrome")
else:
    print("no is not pallindrome")
    
