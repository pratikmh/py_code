import re
txt="the rain98 in the34 spain"
x=re.split('\s',txt)
print(x)
y=re.split('\d+',txt,1)
print(y)
z=re.split('in',txt,2)
print(z)
