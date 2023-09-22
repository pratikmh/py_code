try:
    a=5
    b=0
    print(a/b)
except TypeError:
    print("unsupported operation")
except ZeroDivisionError:
    print("unsupported operationss")
print("out of try except block")
