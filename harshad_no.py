n=int(input("enter no"))
add=0
for i in str(n):
    add=add+int(i)
print(add)
if n%add==0:
    print("harshad")
else:
    print("not harshad")
