from unittest import skip


n=int(input("enter no"))
list1=[]
for i in range(1,n+1):
    if n%i==0:
        # print("factors=",i)
        if i  not in list1:
                    list1.append(i)
print("factors=",list1)
for y in list1:
    for z in range(2,y):
        if y%z==0:
            break
    else:
        print("prime factors=",y,end="")
        
                


             
            
