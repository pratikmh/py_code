n=int(input("enter no"))
m=""
square=n**2
print(square)
length=len(str(n))
# print(length)
for i in range(0,length):
    rem=int(square%10)
    square=square//10
    m=str(rem)+str(m)
print(m)
print(n)
if int(m)==int(n):
    print("automorphic")
else:
    print(" not automorphic")