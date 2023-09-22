def fehr(Cel):
    f=(cel*(9/5)+32)
    return f
cel=int(input("enter celcius"))
fer=fehr(cel)
print(cel,"celsius to fehrenheit is",fer)
