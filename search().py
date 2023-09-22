import re
txt="the rain in the spain"
x=re.search('\s',txt)
print(x.start())
y=re.search('portugal',txt)
print(y)
z=re.search('rain',txt)
print(z)
