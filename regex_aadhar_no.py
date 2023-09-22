import re
aadhar_no='9878 6556 4325'
pattern='[0-9]{4}\s[0-9]{4}\s[0-9]{4}'
result=re.match(pattern,aadhar_no)
if result:
    print("valid aadhar no")
else:
    print("invalid aadhar no")
