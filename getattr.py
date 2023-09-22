class person:
    name="pratik"
    age=22
    country="India"
x=getattr(person,'age','my message')
y=getattr(person,'page','my message')
print('x',x)
print('y',y)

print()
#set attribute
a=setattr(person,'age',23)
b=setattr(person,'gender','male')
print(person.age)
print(person.gender)

print()
#hasattr

p=hasattr(person,'gender')
print(p)
q=hasattr(person,'address')
print(q)

print()
#delattr

delattr(person,'gender')
r=hasattr(person,'gender')
print(r)
