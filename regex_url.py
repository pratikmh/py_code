import re
url='www.mhaskewadi.com'
pattern='(www.|http://|https://)+[A-Za-z0-9]+(.co|.in|.com)+'
result=re.fullmatch(pattern,url)
if result:
    print("valid url")
else:
    print("invalid url")
