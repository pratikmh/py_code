import re
txt="the rain in the spain"
x=re.findall('\s',txt)
print(x)
y=re.findall('portugal',txt)
print(y)
z=re.findall('in',txt)
print(z)
