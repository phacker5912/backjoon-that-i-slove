a=input("")
b=""
for i in a:
    if i.isupper()==True :
        b=b+i.lower()
    else:
        b=b+i.upper()
print(b)

