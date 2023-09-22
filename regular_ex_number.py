import re
no='+917-8787988765'
pattern='[+][0-9]{2,3}[-][7-9][0-9]{9}'
result=re.fullmatch(pattern,no)
if result:
    print("valid number")
else:
    print("invalid number")

print()


no='0255-879889'
pattern='[0][2-5]{2,5}[-][0-9]{6,8}'
result=re.fullmatch(pattern,no)
if result:
    print("valid number")
else:
    print("invalid number")

