import math
n=int(input("enter no"))
root=math.sqrt(n)
if int(root)**2==n:
    print("perfect square")
else:
    print("not perfect")