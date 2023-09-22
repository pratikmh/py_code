def mygenerator():
    print("first item")
    yield 10
    print("second item")
    yield 30
    print("last item")
    yield 50
gen=mygenerator()
print(next(gen))
print(next(gen))
print(next(gen))
