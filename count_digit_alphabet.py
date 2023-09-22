digit=0
alpha=0
sentence=input("enter sentance contain alphabet and digits")
for i in sentence:
    if i.isdigit():
        digit=digit+1
    elif i.isalpha():
        alpha=alpha+1
    else:
        pass
print("total no of digit=",digit)
print("total no of alphabet=",alpha)