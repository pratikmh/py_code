# n=int(input("enter no"))
for n in range(1,1000):
  num=n
  b=0
  l=len(str(n))
  while n>0:
    rem=n%10
    a=rem**l
    n=n//10
    b=b+a
  # print(b)
  if num==b:
     print(b,end=" ")
# else:
#     print("No its not armstrong no")