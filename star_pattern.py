for i in range(5):
    print("*"* (i+1))
print(" ")
n=5
for i in range(n):
    print(" "*(n-i-1),end="")
    print("*"*(2*i+1),end="")
    print(" "*(n-i-1))
print("\n")
print("*"," ","*"," ","*")
print("*"," "," "," ","*")
print("*"," ","*"," ","*")
print("\n")
n=5
for i in range(n):
    print("*"* (i+1))
#print(" ")
for i in range(n,0,-1):    
    #for j in range(0, i - 1):  
    print("*"*i)  
print(" ") 

n=5
for i in range(n):
    print(" "*(n-i-1),end="")
    print("*"*(2*i+1),end="")
    print(" "*(n-i-1))
for i in range(n,0,-1):
    print(" "*(n-i-1),end="")
    print("*"*(2*i+1),end="")
    print(" "*(n-i-1))



