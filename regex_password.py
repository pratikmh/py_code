import re
password='Pratik@123'
pattern='^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}'
result=re.fullmatch(pattern,password)
if result:
    print("valid password")
else:
    print("invalid password")
