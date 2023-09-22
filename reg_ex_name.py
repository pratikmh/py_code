import re
name='Pratik Shivaji Mhaske'
pattern='[A-Za-z]+\s[A-Za-z]+\s[A-Za-z]+'
result=re.match(pattern,name)
if result:
    print("valid name")
else:
    print("invalid name")
