a=int(input("enter a"))
b=int(input("enter b"))
c=int(input("enter c"))
def maxx(a,b,c):
        if a>b:
            if a>c:
                return a
            #else:
                #return c       
        
        elif b>c:
            return b
        else:
            return c
m=maxx(a,b,c)
print("greater is",m)

