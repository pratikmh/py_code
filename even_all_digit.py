# i=2000
# while(i<=3000):
#   no=i
#   count=0
#   while(no):
#      rem=no%10
#      if rem%2==0:
#       count=count+1
#      no=no//10
#   if count==4:
#       print(i,end=" ")
#   i=i+1

    
    

#this code is working properly
# num=2000
# while(num<=3000):
#   no=num
#   j=0
#   while(no):
#     rem=no%10
#     if rem%2==0:
#       j=j+1
#     no=int(no/10)
#   if(j==4):
#     print(num,end=" ")
#   num=num+1




digit=[]
for i in range(2000,3000):
  a=str(i)
  if(int(a[0])%2==0 and int(a[1])%2==0 and int(a[2])%2==0 and int(a[3])%2==0 ):
    digit.append(a)
print(digit)