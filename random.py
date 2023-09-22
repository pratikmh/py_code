import string
import random
print("single letter")
print(random.choice(string.ascii_letters))
print("random length string")
str1=''
for i in range(random.randint(1,20)):
    str1+=(random.choice(string.ascii_letters))
print(str1)
print("fixed length string")
str2=""
for i in range(5):
    str2+=(random.choice(string.ascii_letters))
print(str2)