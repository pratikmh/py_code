n=int(input("enter no 1"))
m=int(input("enter no 2"))
list1=[]
hcf=0
greater=max(m,n)
for i in range(1,greater):
    if m%i==0 and n%i==0:
       hcf=i
print("hcf=",hcf)
        # list1.append(str(i))
# print(list1)
# lcf=max[int(list1)]
# print(lcf)