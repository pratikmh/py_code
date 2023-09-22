
for n in range(1,30):
    if n>2:
        for i in range(2,n):
            if n%i==0:
              break
        else:
             print(n,end=" ")
