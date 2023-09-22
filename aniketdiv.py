try:
    print('try block')
    a=int(input('Enter a number: '))
    b=int(input('Enter anothger number: '))
    c=a/b
except ZeroDivisionError:
    print('Except ZeroDivisionError block')
    print('Division by 0 not accepted')
else:
    print("else block")
    print("Division = ",c)
finally:
    print("Finally block")
    a=0
    b=0
print("Out of try, except else and finally blocks:")
    
