import re
mail='Pratik171.@Gmail.In'
pattern=r'([A-Za-z0-9]|[.!@#$%^&*])+[@][A-Za-z0-9]+([.][A-Z|a-z]{2,})+'
result=re.match(pattern,mail)
if result:
    print("valid email")
else:
    print("invalid email")
