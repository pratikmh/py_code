n=int(input("enter binary number"))
m=n
dec=0
base=1
while n>0:
    rem=n%10
    dec=dec+rem*base
    n=n//10
    base=base*2
print("binary:",m)
print("decimal",dec)


# octal to decimal
n=int(input("enter binary number"))
m=n
dec=0
base=1
while n>0:
    rem=n%10
    dec=dec+rem*base
    n=n//10
    base=base*8
print("binary:",m)
print("decimal",dec)
