n=int(input("enter no to be reverse"))
rev=0
while n>0:
    rem=n%10
    rev=(rev*10)+rem
    n=int(n/10)
print(rev)
    
