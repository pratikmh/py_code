try:
    a=int(input("Enter a number upto 100:"))
    if a > 100:
        raise ValueError(a)
except ValueError:
    print(a,"is out of allowed range")
else:
    print(a,"is within the range")
