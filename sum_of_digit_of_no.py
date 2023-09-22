# no=int(input("enter number"))
# sum=0
# for i in str(no):
#     sum=sum+int(i)
# print(sum)

no=int(input("enter number"))
sum=0
while no>0:
    rem=int(no%10)
    sum=sum+rem
    no=no/10
print(sum)

# no=int(input("enter number"))
# sum=0
# def sum_digit(no,sum):
#     rem=int(no%10)
#     sum=sum+rem
#     return(no/10 ,sum)
# print(sum_digit(no,sum))
