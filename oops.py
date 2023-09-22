class myclass:
    def __init__(myself,name,age):
        myself.name=name
        myself.age=age
    def get_data(myself):
        print(f'{myself.name} {myself.age}')
    def __del__(myself):
        print("destroyed")
name=input("enter name")
age=input("enter age")
a=myclass(name,age)
print(a.name, end="")
print(a.age)
#name=input("enter name")
#age=input("enter age")
#b=myclass(name,age)
#b.get_data()
del a
