n=int(input("enter no"))
a=1
b=2
d=[]
if n>0:
  for i in range(0,n): 
    print(a)
    if a not in d:
        d.append(a)
    c=a+b
    a=b
    b=c
    
else:
    print("enter positive no")
print("fibonacci serie=",d)
m=int(input("enter nth term"))
print(d[m-1])

# n= int(input("enter no of terms? "))

# n1, n2 = 1, 2
# count = 0

# if n >= 0:
#    while count < n:
#        print(n1)
#        nth = n1 + n2
#        n1 = n2
#        n2 = nth
#        count=count+ 1